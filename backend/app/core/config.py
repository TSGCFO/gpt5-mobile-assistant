"""
Application Configuration
Loads and validates environment variables using Pydantic Settings
"""

from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field, field_validator
import json


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    APP_NAME: str = Field(default="GPT5-Mobile-Assistant", description="Application name")
    DEBUG: bool = Field(default=False, description="Debug mode")
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")

    # OpenAI
    OPENAI_API_KEY: str = Field(..., description="OpenAI API key")
    OPENAI_MODEL: str = Field(default="gpt-5", description="Default OpenAI model")
    OPENAI_REASONING_EFFORT: str = Field(
        default="medium",
        description="Reasoning effort level: low, medium, high"
    )

    # Database
    DATABASE_URL: str = Field(..., description="PostgreSQL connection string")

    # Redis
    REDIS_URL: str = Field(default="redis://localhost:6379/0", description="Redis connection string")
    REDIS_PASSWORD: str = Field(default="", description="Redis password")
    REDIS_CACHE_TTL: int = Field(default=1800, description="Cache TTL in seconds (default 30 minutes)")

    # CORS
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:19000"],
        description="Allowed CORS origins"
    )

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = Field(default=60, description="Rate limit per user per minute")

    # Server
    HOST: str = Field(default="0.0.0.0", description="Server host")
    PORT: int = Field(default=8000, description="Server port")
    WORKERS: int = Field(default=1, description="Number of worker processes")

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        """Parse CORS origins from JSON string if needed"""
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [origin.strip() for origin in v.split(",")]
        return v

    @field_validator("OPENAI_REASONING_EFFORT")
    @classmethod
    def validate_reasoning_effort(cls, v):
        """Validate reasoning effort level"""
        valid_levels = ["low", "medium", "high"]
        if v not in valid_levels:
            raise ValueError(f"OPENAI_REASONING_EFFORT must be one of {valid_levels}")
        return v

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


# Global settings instance
settings = Settings()


# Helper functions
def get_settings() -> Settings:
    """
    Get application settings instance.
    Use this as a FastAPI dependency.

    Example:
        @app.get("/config")
        def read_config(settings: Settings = Depends(get_settings)):
            return {"app_name": settings.APP_NAME}
    """
    return settings
