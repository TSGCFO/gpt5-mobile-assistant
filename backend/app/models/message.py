"""
Message Model
Represents individual chat messages within conversations
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.db.database import Base


class Message(Base):
    """
    Message model for chat messages.

    Attributes:
        id: Unique message identifier (UUID)
        conversation_id: Foreign key to parent conversation
        role: Message role ('user' or 'assistant')
        content: Message text content
        message_metadata: Additional data (tokens, model, citations, tool_calls)
        created_at: Message creation timestamp
        conversation: Relationship to Conversation model
    """

    __tablename__ = "messages"

    # Primary Key
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        comment="Unique message identifier"
    )

    # Foreign Keys
    conversation_id = Column(
        UUID(as_uuid=True),
        ForeignKey("conversations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Parent conversation"
    )

    # Message Data
    role = Column(
        String(20),
        nullable=False,
        comment="Message role: 'user' or 'assistant'"
    )

    content = Column(
        Text,
        nullable=False,
        comment="Message text content"
    )

    message_metadata = Column(
        JSONB,
        nullable=False,
        default=dict,
        comment="Additional data: tokens, model, citations, tool_calls"
    )

    # Timestamps
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="Message creation timestamp"
    )

    # Relationships
    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )

    def __repr__(self):
        content_preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
        return f"<Message(id={self.id}, role={self.role}, content='{content_preview}')>"

    def to_dict(self):
        """Convert message to dictionary"""
        return {
            "id": str(self.id),
            "conversation_id": str(self.conversation_id),
            "role": self.role,
            "content": self.content,
            "metadata": self.message_metadata,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
