"""
Authentication Schemas
Pydantic models for user registration, login, and response
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator


class UserCreate(BaseModel):
    """Schema for user registration"""

    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_-]+$",
        description="Username (3-50 characters, alphanumeric, underscore, hyphen)"
    )

    email: EmailStr = Field(
        ...,
        description="Valid email address"
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="Password (min 8 characters)"
    )

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v):
        """Validate password strength requirements"""
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        return v

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "username": "john_doe",
                "email": "john@example.com",
                "password": "SecurePass123"
            }]
        }
    }


class UserLogin(BaseModel):
    """Schema for user login"""

    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Username"
    )

    password: str = Field(
        ...,
        min_length=1,
        description="Password"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "username": "john_doe",
                "password": "SecurePass123"
            }]
        }
    }


class UserResponse(BaseModel):
    """Schema for user response (excludes password)"""

    id: str = Field(..., description="User unique identifier")
    username: str = Field(..., description="Username")
    email: str = Field(..., description="Email address")
    created_at: datetime = Field(..., description="Account creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [{
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "username": "john_doe",
                "email": "john@example.com",
                "created_at": "2025-01-01T12:00:00Z",
                "updated_at": "2025-01-01T12:00:00Z"
            }]
        }
    }
