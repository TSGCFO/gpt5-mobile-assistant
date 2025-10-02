"""
Chat Endpoints
GPT-5 chat completions with streaming support
"""

import json
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.middleware.auth_middleware import get_current_user
from app.models.user import User
from app.models.conversation import Conversation
from app.schemas.chat import ChatRequest, ChatResponse, StreamChatRequest, UsageInfo, URLCitation
from app.services.openai_service import OpenAIService, get_openai_service
from app.services.memory_service import MemoryService, get_memory_service
from app.utils.cache import RedisCache, get_cache
from app.core.logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.post(
    "/completions",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
    tags=["Chat"],
    summary="Create chat completion",
    description="Get a response from GPT-5 with optional web search and code interpreter"
)
async def create_chat_completion(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    openai_service: OpenAIService = Depends(get_openai_service),
    cache: RedisCache = Depends(get_cache)
):
    """
    Create a chat completion.

    Features:
    - GPT-5 with configurable reasoning effort
    - Web search with citations
    - Code interpreter (Python execution)
    - Conversation memory management

    Args:
        request: Chat request with message and settings
        current_user: Authenticated user
        db: Database session
        openai_service: OpenAI service instance
        cache: Redis cache instance

    Returns:
        Chat response with message, usage, and citations

    Raises:
        404: Conversation not found
        500: OpenAI API or database error
    """
    try:
        # Create or get conversation
        conversation_id = request.conversation_id

        if conversation_id:
            # Verify conversation exists and belongs to user
            conversation = db.query(Conversation)\
                .filter(
                    Conversation.id == conversation_id,
                    Conversation.user_id == current_user.id
                )\
                .first()

            if not conversation:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Conversation not found"
                )
        else:
            # Create new conversation
            conversation = Conversation(
                user_id=current_user.id,
                title=None  # Will be generated from first message
            )
            db.add(conversation)
            db.commit()
            db.refresh(conversation)
            conversation_id = str(conversation.id)
            logger.info(f"Created new conversation: {conversation_id}")

        # Get conversation context from memory
        memory_service = MemoryService(db, cache)
        context = await memory_service.get_conversation_context(conversation_id)

        # Add user's new message to context
        context.append({
            "role": "user",
            "content": request.message
        })

        # Save user message to database
        await memory_service.save_message(
            conversation_id=conversation_id,
            role="user",
            content=request.message
        )

        # Generate conversation title if this is the first user message
        if not conversation.title:
            await memory_service.create_conversation_title(
                conversation_id=conversation_id,
                first_message=request.message
            )

        # Call OpenAI API
        logger.info(
            f"Creating response for conversation {conversation_id}, "
            f"context length: {len(context)} messages"
        )

        response = await openai_service.create_response(
            messages=context,
            reasoning_effort=request.reasoning_effort,
            use_web_search=request.use_web_search,
            use_code_interpreter=request.use_code_interpreter,
            mcp_servers=request.mcp_servers
        )

        # Save assistant message to database
        assistant_message = await memory_service.save_message(
            conversation_id=conversation_id,
            role="assistant",
            content=response["output_text"],
            metadata={
                "usage": response["usage"],
                "citations": response["citations"],
                "model": "gpt-5"
            }
        )

        logger.info(
            f"Response created successfully for conversation {conversation_id}, "
            f"tokens: {response['usage']['total_tokens']}"
        )

        # Format response
        return ChatResponse(
            message=response["output_text"],
            conversation_id=conversation_id,
            message_id=str(assistant_message.id),
            usage=UsageInfo(**response["usage"]),
            citations=[URLCitation(**cite) for cite in response["citations"]],
            metadata={"model": "gpt-5"}
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Chat completion error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create chat completion: {str(e)}"
        )


@router.post(
    "/stream",
    status_code=status.HTTP_200_OK,
    tags=["Chat"],
    summary="Stream chat completion",
    description="Stream responses from GPT-5 using Server-Sent Events (SSE)"
)
async def stream_chat_completion(
    request: StreamChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    openai_service: OpenAIService = Depends(get_openai_service),
    cache: RedisCache = Depends(get_cache)
):
    """
    Stream a chat completion using Server-Sent Events.

    This endpoint returns events as they are generated, allowing for
    real-time display of the response.

    Event types:
    - response.output_text.delta: Text chunks being generated
    - response.output_text.done: Text generation complete
    - response.completed: Full response complete with usage info
    - error: Error occurred during generation

    Args:
        request: Stream chat request with messages
        current_user: Authenticated user
        db: Database session
        openai_service: OpenAI service instance
        cache: Redis cache instance

    Returns:
        StreamingResponse with Server-Sent Events

    Raises:
        404: Conversation not found
    """
    async def generate():
        """Generator function for SSE streaming"""
        try:
            # Create or get conversation
            conversation_id = request.conversation_id

            if conversation_id:
                conversation = db.query(Conversation)\
                    .filter(
                        Conversation.id == conversation_id,
                        Conversation.user_id == current_user.id
                    )\
                    .first()

                if not conversation:
                    error_event = {
                        "type": "error",
                        "error": "Conversation not found"
                    }
                    yield f"data: {json.dumps(error_event)}\n\n"
                    return
            else:
                # Create new conversation
                conversation = Conversation(user_id=current_user.id)
                db.add(conversation)
                db.commit()
                db.refresh(conversation)
                conversation_id = str(conversation.id)

                # Send conversation ID to client
                init_event = {
                    "type": "conversation.created",
                    "conversation_id": conversation_id
                }
                yield f"data: {json.dumps(init_event)}\n\n"

            # Save messages and create streaming response
            memory_service = MemoryService(db, cache)

            # Save user messages
            for msg in request.messages:
                if msg.role == "user":
                    await memory_service.save_message(
                        conversation_id=conversation_id,
                        role=msg.role,
                        content=msg.content
                    )

            logger.info(f"Starting stream for conversation {conversation_id}")

            # Stream from OpenAI
            accumulated_text = ""
            usage_info = None

            async for event in openai_service.create_streaming_response(
                messages=[{"role": m.role, "content": m.content} for m in request.messages],
                reasoning_effort=request.reasoning_effort,
                use_web_search=request.use_web_search,
                use_code_interpreter=request.use_code_interpreter,
                mcp_servers=request.mcp_servers
            ):
                # Accumulate text for saving
                if event.get("type") == "response.output_text.delta":
                    accumulated_text += event.get("text_delta", "")

                # Capture usage info
                if event.get("usage"):
                    usage_info = event["usage"]

                # Send event to client
                yield f"data: {json.dumps(event)}\n\n"

            # Save assistant message
            if accumulated_text:
                await memory_service.save_message(
                    conversation_id=conversation_id,
                    role="assistant",
                    content=accumulated_text,
                    metadata={
                        "usage": usage_info,
                        "model": "gpt-5",
                        "streaming": True
                    }
                )

                # Generate title if needed
                if not conversation.title:
                    first_user_msg = next(
                        (m.content for m in request.messages if m.role == "user"),
                        None
                    )
                    if first_user_msg:
                        await memory_service.create_conversation_title(
                            conversation_id=conversation_id,
                            first_message=first_user_msg
                        )

            logger.info(f"Stream completed for conversation {conversation_id}")

        except Exception as e:
            logger.error(f"Streaming error: {str(e)}")
            error_event = {
                "type": "error",
                "error": str(e)
            }
            yield f"data: {json.dumps(error_event)}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )
