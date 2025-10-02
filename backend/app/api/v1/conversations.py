"""
Conversations Endpoints
Manage conversation history and messages
"""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.middleware.auth_middleware import get_current_user
from app.models.user import User
from app.models.conversation import Conversation
from app.schemas.conversation import (
    ConversationCreate,
    ConversationResponse,
    ConversationListResponse,
    MessageResponse
)
from app.services.memory_service import MemoryService, get_memory_service
from app.utils.cache import RedisCache, get_cache
from app.core.logging_config import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get(
    "",
    response_model=ConversationListResponse,
    status_code=status.HTTP_200_OK,
    tags=["Conversations"],
    summary="List conversations",
    description="Get a list of all conversations for the authenticated user"
)
async def list_conversations(
    limit: int = Query(default=50, ge=1, le=100, description="Number of conversations to return"),
    offset: int = Query(default=0, ge=0, description="Number of conversations to skip"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    List user's conversations with pagination.

    Args:
        limit: Maximum number of conversations (1-100)
        offset: Number of conversations to skip
        current_user: Authenticated user
        db: Database session

    Returns:
        List of conversations with metadata

    Raises:
        401: Not authenticated
    """
    try:
        # Get conversations
        conversations = db.query(Conversation)\
            .filter(Conversation.user_id == current_user.id)\
            .order_by(Conversation.updated_at.desc())\
            .offset(offset)\
            .limit(limit)\
            .all()

        # Get total count
        total = db.query(Conversation)\
            .filter(Conversation.user_id == current_user.id)\
            .count()

        # Convert to response format
        conv_responses = [
            ConversationResponse(
                id=str(conv.id),
                user_id=str(conv.user_id),
                title=conv.title,
                created_at=conv.created_at,
                updated_at=conv.updated_at,
                message_count=conv.messages.count()
            )
            for conv in conversations
        ]

        logger.info(f"Retrieved {len(conv_responses)} conversations for user {current_user.username}")

        return ConversationListResponse(
            conversations=conv_responses,
            total=total
        )

    except Exception as e:
        logger.error(f"Error listing conversations: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve conversations"
        )


@router.post(
    "",
    response_model=ConversationResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Conversations"],
    summary="Create conversation",
    description="Create a new conversation"
)
async def create_conversation(
    conversation_data: ConversationCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new conversation.

    Args:
        conversation_data: Conversation creation data (optional title)
        current_user: Authenticated user
        db: Database session

    Returns:
        Created conversation details

    Raises:
        401: Not authenticated
        500: Database error
    """
    try:
        # Create conversation
        conversation = Conversation(
            user_id=current_user.id,
            title=conversation_data.title
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        logger.info(f"Created conversation {conversation.id} for user {current_user.username}")

        return ConversationResponse(
            id=str(conversation.id),
            user_id=str(conversation.user_id),
            title=conversation.title,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at,
            message_count=0
        )

    except Exception as e:
        db.rollback()
        logger.error(f"Error creating conversation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create conversation"
        )


@router.get(
    "/{conversation_id}",
    response_model=ConversationResponse,
    status_code=status.HTTP_200_OK,
    tags=["Conversations"],
    summary="Get conversation",
    description="Get a specific conversation by ID"
)
async def get_conversation(
    conversation_id: str,
    include_messages: bool = Query(default=False, description="Include messages in response"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a specific conversation.

    Args:
        conversation_id: Conversation UUID
        include_messages: Whether to include messages
        current_user: Authenticated user
        db: Database session

    Returns:
        Conversation details with optional messages

    Raises:
        401: Not authenticated
        404: Conversation not found
    """
    try:
        # Get conversation
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

        # Build response
        response = ConversationResponse(
            id=str(conversation.id),
            user_id=str(conversation.user_id),
            title=conversation.title,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at,
            message_count=conversation.messages.count()
        )

        # Include messages if requested
        if include_messages:
            messages = conversation.messages.all()
            response.messages = [
                MessageResponse(
                    id=str(msg.id),
                    conversation_id=str(msg.conversation_id),
                    role=msg.role,
                    content=msg.content,
                    metadata=msg.metadata,
                    created_at=msg.created_at
                )
                for msg in messages
            ]

        return response

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting conversation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve conversation"
        )


@router.delete(
    "/{conversation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Conversations"],
    summary="Delete conversation",
    description="Delete a conversation and all its messages"
)
async def delete_conversation(
    conversation_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    cache: RedisCache = Depends(get_cache)
):
    """
    Delete a conversation and all its messages.

    Args:
        conversation_id: Conversation UUID
        current_user: Authenticated user
        db: Database session
        cache: Redis cache instance

    Raises:
        401: Not authenticated
        404: Conversation not found
        500: Database error
    """
    try:
        # Get conversation
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

        # Delete from database (messages cascade)
        db.delete(conversation)
        db.commit()

        # Clear cache
        memory_service = MemoryService(db, cache)
        await memory_service.clear_conversation_cache(conversation_id)

        logger.info(f"Deleted conversation {conversation_id} for user {current_user.username}")

        return None

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting conversation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete conversation"
        )


@router.get(
    "/{conversation_id}/messages",
    response_model=list[MessageResponse],
    status_code=status.HTTP_200_OK,
    tags=["Conversations"],
    summary="Get conversation messages",
    description="Get all messages in a conversation"
)
async def get_conversation_messages(
    conversation_id: str,
    limit: Optional[int] = Query(default=None, ge=1, le=100, description="Max messages to return"),
    offset: int = Query(default=0, ge=0, description="Number of messages to skip"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    cache: RedisCache = Depends(get_cache)
):
    """
    Get messages for a conversation with pagination.

    Args:
        conversation_id: Conversation UUID
        limit: Maximum messages to return (None = all)
        offset: Number of messages to skip
        current_user: Authenticated user
        db: Database session
        cache: Redis cache instance

    Returns:
        List of messages

    Raises:
        401: Not authenticated
        404: Conversation not found
    """
    try:
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

        # Get messages
        memory_service = MemoryService(db, cache)
        messages = await memory_service.get_conversation_messages(
            conversation_id=conversation_id,
            limit=limit,
            offset=offset
        )

        # Convert to response format
        message_responses = [
            MessageResponse(
                id=str(msg.id),
                conversation_id=str(msg.conversation_id),
                role=msg.role,
                content=msg.content,
                metadata=msg.metadata,
                created_at=msg.created_at
            )
            for msg in messages
        ]

        logger.info(f"Retrieved {len(message_responses)} messages for conversation {conversation_id}")

        return message_responses

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting messages: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve messages"
        )
