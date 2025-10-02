"""
Memory Service
Dual-tier memory system: PostgreSQL (long-term) + Redis (working memory)
"""

import json
from typing import List, Dict, Optional, Any
from sqlalchemy.orm import Session
from app.models.conversation import Conversation
from app.models.message import Message
from app.utils.cache import RedisCache
from app.core.logging_config import get_logger
from app.core.exceptions import DatabaseError, NotFoundError

logger = get_logger(__name__)


class MemoryService:
    """
    Service for managing conversation memory across PostgreSQL and Redis.

    Features:
    - Long-term memory: PostgreSQL for persistent storage
    - Working memory: Redis for fast context retrieval
    - Automatic cache invalidation
    - Context window management
    """

    def __init__(self, db: Session, cache: RedisCache):
        """
        Initialize memory service.

        Args:
            db: SQLAlchemy database session
            cache: Redis cache instance
        """
        self.db = db
        self.cache = cache
        self.context_cache_ttl = 1800  # 30 minutes

    async def get_conversation_context(
        self,
        conversation_id: str,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Get conversation messages as context for OpenAI API.
        Checks Redis cache first, falls back to PostgreSQL.

        Args:
            conversation_id: Conversation UUID
            limit: Maximum number of messages to retrieve

        Returns:
            List of message dictionaries in OpenAI format:
            [{"role": "user", "content": "..."}, ...]
        """
        cache_key = f"conv:{conversation_id}:context"

        try:
            # Try Redis cache first
            cached = await self.cache.get(cache_key)
            if cached:
                logger.debug(f"Context cache hit for conversation {conversation_id}")
                return cached

            # Cache miss - fetch from PostgreSQL
            logger.debug(f"Context cache miss for conversation {conversation_id}, fetching from DB")

            messages = self.db.query(Message)\
                .filter(Message.conversation_id == conversation_id)\
                .order_by(Message.created_at.desc())\
                .limit(limit)\
                .all()

            # Convert to OpenAI format (reverse to chronological order)
            context = [
                {
                    "role": msg.role,
                    "content": msg.content
                }
                for msg in reversed(messages)
            ]

            # Cache the context
            await self.cache.set(cache_key, context, ttl=self.context_cache_ttl)

            logger.info(f"Retrieved {len(context)} messages for conversation {conversation_id}")
            return context

        except Exception as e:
            logger.error(f"Error getting conversation context: {str(e)}")
            raise DatabaseError(
                message="Failed to retrieve conversation context",
                details={"conversation_id": conversation_id, "error": str(e)}
            )

    async def save_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Message:
        """
        Save a message to PostgreSQL and invalidate cache.

        Args:
            conversation_id: Conversation UUID
            role: Message role ('user' or 'assistant')
            content: Message text content
            metadata: Additional metadata (tokens, citations, etc.)

        Returns:
            Created Message object

        Raises:
            DatabaseError: If save fails
        """
        try:
            # Create message
            message = Message(
                conversation_id=conversation_id,
                role=role,
                content=content,
                metadata=metadata or {}
            )

            self.db.add(message)
            self.db.commit()
            self.db.refresh(message)

            # Invalidate cache
            cache_key = f"conv:{conversation_id}:context"
            await self.cache.delete(cache_key)

            # Update conversation updated_at
            conversation = self.db.query(Conversation)\
                .filter(Conversation.id == conversation_id)\
                .first()
            if conversation:
                self.db.commit()  # This triggers the updated_at onupdate

            logger.info(
                f"Message saved: conversation={conversation_id}, "
                f"role={role}, length={len(content)}"
            )

            return message

        except Exception as e:
            self.db.rollback()
            logger.error(f"Error saving message: {str(e)}")
            raise DatabaseError(
                message="Failed to save message",
                details={"conversation_id": conversation_id, "error": str(e)}
            )

    async def get_conversation_messages(
        self,
        conversation_id: str,
        limit: Optional[int] = None,
        offset: int = 0
    ) -> List[Message]:
        """
        Get messages for a conversation with pagination.

        Args:
            conversation_id: Conversation UUID
            limit: Maximum number of messages (None = all)
            offset: Number of messages to skip

        Returns:
            List of Message objects
        """
        try:
            query = self.db.query(Message)\
                .filter(Message.conversation_id == conversation_id)\
                .order_by(Message.created_at.asc())\
                .offset(offset)

            if limit:
                query = query.limit(limit)

            messages = query.all()

            logger.debug(f"Retrieved {len(messages)} messages for conversation {conversation_id}")
            return messages

        except Exception as e:
            logger.error(f"Error getting messages: {str(e)}")
            raise DatabaseError(
                message="Failed to retrieve messages",
                details={"conversation_id": conversation_id, "error": str(e)}
            )

    async def create_conversation_title(
        self,
        conversation_id: str,
        first_message: str
    ) -> str:
        """
        Generate a conversation title from the first message.

        Args:
            conversation_id: Conversation UUID
            first_message: First user message

        Returns:
            Generated title (truncated to 60 characters)
        """
        try:
            # Simple title generation: take first 60 chars of first message
            # TODO: Could use OpenAI to generate more meaningful titles
            title = first_message[:60].strip()
            if len(first_message) > 60:
                title += "..."

            # Update conversation
            conversation = self.db.query(Conversation)\
                .filter(Conversation.id == conversation_id)\
                .first()

            if conversation and not conversation.title:
                conversation.title = title
                self.db.commit()
                logger.info(f"Generated title for conversation {conversation_id}: {title}")

            return title

        except Exception as e:
            logger.error(f"Error creating conversation title: {str(e)}")
            # Non-critical error, return default title
            return "New Conversation"

    async def clear_conversation_cache(self, conversation_id: str):
        """
        Clear Redis cache for a conversation.

        Args:
            conversation_id: Conversation UUID
        """
        cache_key = f"conv:{conversation_id}:context"
        await self.cache.delete(cache_key)
        logger.debug(f"Cleared cache for conversation {conversation_id}")

    async def get_user_conversation_count(self, user_id: str) -> int:
        """
        Get total number of conversations for a user.

        Args:
            user_id: User UUID

        Returns:
            Number of conversations
        """
        try:
            count = self.db.query(Conversation)\
                .filter(Conversation.user_id == user_id)\
                .count()

            return count

        except Exception as e:
            logger.error(f"Error counting conversations: {str(e)}")
            return 0


def get_memory_service(
    db: Session,
    cache: RedisCache
) -> MemoryService:
    """
    Create memory service instance.
    Use as FastAPI dependency with Depends.

    Example:
        @app.get("/messages")
        async def get_messages(
            memory: MemoryService = Depends(get_memory_service)
        ):
            return await memory.get_conversation_messages(conv_id)
    """
    return MemoryService(db=db, cache=cache)
