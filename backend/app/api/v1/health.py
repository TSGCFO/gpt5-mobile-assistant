"""
Health Check Endpoint
Simple endpoint to verify API is running
"""

from fastapi import APIRouter, status
from app.core.config import settings
from datetime import datetime

router = APIRouter()


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    tags=["Health"],
    summary="Health check",
    description="Check if API is running and responsive"
)
async def health_check():
    """
    Health check endpoint.
    Returns API status and basic information.
    No authentication required.
    """
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "timestamp": datetime.utcnow().isoformat(),
        "model": settings.OPENAI_MODEL,
    }
