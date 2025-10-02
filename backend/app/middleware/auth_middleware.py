"""
Authentication Middleware
Basic HTTP Authentication for protecting endpoints
"""

from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.services.auth_service import AuthService, get_auth_service
from app.core.logging_config import get_logger

logger = get_logger(__name__)

# HTTP Basic Authentication scheme
security = HTTPBasic()


async def get_current_user(
    credentials: HTTPBasicCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Authenticate user with HTTP Basic Authentication.
    Username and password are sent with each request in Authorization header.

    Args:
        credentials: HTTP Basic credentials (username, password)
        db: Database session

    Returns:
        Authenticated User object

    Raises:
        HTTPException: 401 if authentication fails

    Usage:
        @app.get("/protected")
        def protected_route(user: User = Depends(get_current_user)):
            return {"message": f"Hello {user.username}"}
    """
    try:
        # Create auth service
        auth_service = AuthService(db)

        # Authenticate user
        user = auth_service.authenticate_user(
            username=credentials.username,
            password=credentials.password
        )

        logger.debug(f"User authenticated: {user.username}")
        return user

    except Exception as e:
        logger.warning(
            f"Authentication failed for user: {credentials.username} - {str(e)}"
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


async def get_optional_user(
    credentials: Optional[HTTPBasicCredentials] = Depends(HTTPBasic(auto_error=False)),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """
    Optionally authenticate user (allows unauthenticated access).
    Useful for endpoints that work differently for authenticated vs anonymous users.

    Args:
        credentials: HTTP Basic credentials (optional)
        db: Database session

    Returns:
        User object if authenticated, None otherwise

    Usage:
        @app.get("/public")
        def public_route(user: Optional[User] = Depends(get_optional_user)):
            if user:
                return {"message": f"Hello {user.username}"}
            return {"message": "Hello guest"}
    """
    if credentials is None:
        return None

    try:
        auth_service = AuthService(db)
        user = auth_service.authenticate_user(
            username=credentials.username,
            password=credentials.password
        )
        return user
    except Exception:
        return None
