"""
Authentication Service
User registration, login, and credential verification
"""

from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password, is_password_strong
from app.core.logging_config import get_logger
from app.core.exceptions import (
    AuthenticationError,
    ConflictError,
    ValidationError,
    DatabaseError
)

logger = get_logger(__name__)


class AuthService:
    """
    Service for user authentication operations.

    Features:
    - User registration with validation
    - Password verification
    - Credential management
    """

    def __init__(self, db: Session):
        """
        Initialize authentication service.

        Args:
            db: SQLAlchemy database session
        """
        self.db = db

    def register_user(
        self,
        username: str,
        email: str,
        password: str
    ) -> User:
        """
        Register a new user with validation.

        Args:
            username: Unique username
            email: Unique email address
            password: Plain text password (will be hashed)

        Returns:
            Created User object

        Raises:
            ValidationError: If password is weak
            ConflictError: If username or email already exists
            DatabaseError: If database operation fails
        """
        try:
            # Validate password strength
            is_strong, error_msg = is_password_strong(password)
            if not is_strong:
                raise ValidationError(
                    message=error_msg,
                    details={"field": "password"}
                )

            # Check if username exists
            existing_user = self.db.query(User)\
                .filter(User.username == username)\
                .first()

            if existing_user:
                raise ConflictError(
                    message="Username already exists",
                    details={"field": "username", "value": username}
                )

            # Check if email exists
            existing_email = self.db.query(User)\
                .filter(User.email == email)\
                .first()

            if existing_email:
                raise ConflictError(
                    message="Email already exists",
                    details={"field": "email", "value": email}
                )

            # Hash password
            password_hash = hash_password(password)

            # Create user
            user = User(
                username=username,
                email=email,
                password_hash=password_hash
            )

            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

            logger.info(f"User registered successfully: {username} ({email})")
            return user

        except (ValidationError, ConflictError):
            self.db.rollback()
            raise
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error registering user: {str(e)}")
            raise DatabaseError(
                message="Failed to register user",
                details={"error": str(e)}
            )

    def authenticate_user(
        self,
        username: str,
        password: str
    ) -> User:
        """
        Authenticate user with username and password.

        Args:
            username: Username
            password: Plain text password

        Returns:
            User object if authentication successful

        Raises:
            AuthenticationError: If credentials are invalid
        """
        try:
            # Find user by username
            user = self.db.query(User)\
                .filter(User.username == username)\
                .first()

            if not user:
                logger.warning(f"Authentication failed: user not found - {username}")
                raise AuthenticationError(
                    message="Invalid username or password",
                    details={"username": username}
                )

            # Verify password
            if not verify_password(password, user.password_hash):
                logger.warning(f"Authentication failed: invalid password - {username}")
                raise AuthenticationError(
                    message="Invalid username or password",
                    details={"username": username}
                )

            logger.info(f"User authenticated successfully: {username}")
            return user

        except AuthenticationError:
            raise
        except Exception as e:
            logger.error(f"Error authenticating user: {str(e)}")
            raise AuthenticationError(
                message="Authentication failed",
                details={"error": str(e)}
            )

    def get_user_by_username(self, username: str) -> Optional[User]:
        """
        Get user by username.

        Args:
            username: Username to search

        Returns:
            User object or None if not found
        """
        try:
            return self.db.query(User)\
                .filter(User.username == username)\
                .first()
        except Exception as e:
            logger.error(f"Error getting user by username: {str(e)}")
            return None

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Get user by email.

        Args:
            email: Email to search

        Returns:
            User object or None if not found
        """
        try:
            return self.db.query(User)\
                .filter(User.email == email)\
                .first()
        except Exception as e:
            logger.error(f"Error getting user by email: {str(e)}")
            return None

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Get user by ID.

        Args:
            user_id: User UUID

        Returns:
            User object or None if not found
        """
        try:
            return self.db.query(User)\
                .filter(User.id == user_id)\
                .first()
        except Exception as e:
            logger.error(f"Error getting user by ID: {str(e)}")
            return None


def get_auth_service(db: Session) -> AuthService:
    """
    Create auth service instance.
    Use as FastAPI dependency.

    Example:
        @app.post("/register")
        def register(
            auth: AuthService = Depends(get_auth_service)
        ):
            return auth.register_user(username, email, password)
    """
    return AuthService(db=db)
