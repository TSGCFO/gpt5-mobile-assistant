"""
Conversation Model
Represents chat conversations/threads
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class Conversation(Base):
    """
    Conversation model for organizing chat messages.

    Attributes:
        id: Unique conversation identifier (UUID)
        user_id: Foreign key to user who owns this conversation
        title: Conversation title/summary
        created_at: Conversation creation timestamp
        updated_at: Last message timestamp
        user: Relationship to User model
        messages: Relationship to Message model
    """

    __tablename__ = "conversations"

    # Primary Key
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        comment="Unique conversation identifier"
    )

    # Foreign Keys
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="User who owns this conversation"
    )

    # Conversation Data
    title = Column(
        String(255),
        nullable=True,
        comment="Conversation title/summary (auto-generated from first message)"
    )

    # Timestamps
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
        index=True,
        comment="Conversation creation timestamp"
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        index=True,
        comment="Last message timestamp"
    )

    # Relationships
    user = relationship(
        "User",
        back_populates="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="Message.created_at"
    )

    def __repr__(self):
        return f"<Conversation(id={self.id}, user_id={self.user_id}, title={self.title})>"

    def to_dict(self, include_messages=False):
        """
        Convert conversation to dictionary.

        Args:
            include_messages: Whether to include messages in the response

        Returns:
            Dictionary representation of conversation
        """
        data = {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "title": self.title,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

        if include_messages:
            data["messages"] = [msg.to_dict() for msg in self.messages.all()]
            data["message_count"] = len(data["messages"])

        return data
