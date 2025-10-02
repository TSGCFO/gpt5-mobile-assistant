"""
Conversation Schemas
Pydantic models for conversation management
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ConversationCreate(BaseModel):
    """Schema for creating a new conversation"""

    title: Optional[str] = Field(
        None,
        max_length=255,
        description="Conversation title (auto-generated if not provided)"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "title": "Discussion about AI"
            }]
        }
    }


class MessageResponse(BaseModel):
    """Schema for message response"""

    id: str = Field(..., description="Message unique identifier")
    conversation_id: str = Field(..., description="Parent conversation ID")
    role: str = Field(..., description="Message role: 'user' or 'assistant'")
    content: str = Field(..., description="Message text content")
    metadata: dict = Field(default_factory=dict, description="Additional metadata")
    created_at: datetime = Field(..., description="Message creation timestamp")

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [{
                "id": "456e7890-e89b-12d3-a456-426614174111",
                "conversation_id": "123e4567-e89b-12d3-a456-426614174000",
                "role": "user",
                "content": "Hello, how are you?",
                "metadata": {},
                "created_at": "2025-01-01T12:00:00Z"
            }]
        }
    }


class ConversationResponse(BaseModel):
    """Schema for conversation response"""

    id: str = Field(..., description="Conversation unique identifier")
    user_id: str = Field(..., description="Owner user ID")
    title: Optional[str] = Field(None, description="Conversation title")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    messages: Optional[List[MessageResponse]] = Field(
        None,
        description="List of messages (optional)"
    )
    message_count: Optional[int] = Field(None, description="Total message count")

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [{
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "789e0123-e89b-12d3-a456-426614174222",
                "title": "Discussion about AI",
                "created_at": "2025-01-01T12:00:00Z",
                "updated_at": "2025-01-01T12:30:00Z",
                "message_count": 10
            }]
        }
    }


class ConversationListResponse(BaseModel):
    """Schema for list of conversations"""

    conversations: List[ConversationResponse] = Field(
        ...,
        description="List of conversations"
    )
    total: int = Field(..., description="Total number of conversations")

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "conversations": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "user_id": "789e0123-e89b-12d3-a456-426614174222",
                        "title": "Discussion about AI",
                        "created_at": "2025-01-01T12:00:00Z",
                        "updated_at": "2025-01-01T12:30:00Z"
                    }
                ],
                "total": 1
            }]
        }
    }
