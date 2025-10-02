"""
Authentication Endpoints
User registration and login
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import UserCreate, UserLogin, UserResponse
from app.services.auth_service import AuthService, get_auth_service
from app.middleware.auth_middleware import get_current_user
from app.models.user import User
from app.core.logging_config import get_logger
from app.core.exceptions import ValidationError, ConflictError, AuthenticationError

logger = get_logger(__name__)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Authentication"],
    summary="Register a new user",
    description="Create a new user account with username, email, and password"
)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user.

    Requirements:
    - Username: 3-50 characters, alphanumeric with underscore/hyphen
    - Email: Valid email address
    - Password: Min 8 characters with uppercase, lowercase, and digit

    Returns:
    - User information (excludes password)

    Raises:
    - 400: Weak password
    - 409: Username or email already exists
    - 500: Database error
    """
    try:
        auth_service = AuthService(db)
        user = auth_service.register_user(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password
        )

        logger.info(f"User registered: {user.username}")

        return UserResponse(
            id=str(user.id),
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        )

    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    except ConflictError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message
        )
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register user"
        )


@router.post(
    "/verify",
    response_model=dict,
    status_code=status.HTTP_200_OK,
    tags=["Authentication"],
    summary="Verify credentials",
    description="Verify username and password (used for login validation)"
)
async def verify_credentials(
    user: User = Depends(get_current_user)
):
    """
    Verify user credentials.
    Uses Basic HTTP Authentication.

    This endpoint is called by the frontend during login to verify credentials.
    If successful, the frontend stores credentials for subsequent requests.

    Returns:
    - User information and success message

    Raises:
    - 401: Invalid credentials
    """
    return {
        "message": "Authentication successful",
        "user": UserResponse(
            id=str(user.id),
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    }


@router.get(
    "/me",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    tags=["Authentication"],
    summary="Get current user",
    description="Get information about the currently authenticated user"
)
async def get_current_user_info(
    user: User = Depends(get_current_user)
):
    """
    Get current user information.
    Requires authentication.

    Returns:
    - Current user details

    Raises:
    - 401: Not authenticated
    """
    return UserResponse(
        id=str(user.id),
        username=user.username,
        email=user.email,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
