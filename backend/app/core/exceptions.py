"""
Custom Exception Classes
Define application-specific exceptions for better error handling
"""

from typing import Any, Dict, Optional


class AppException(Exception):
    """Base exception class for all application exceptions"""

    def __init__(
        self,
        message: str,
        status_code: int = 500,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


class AuthenticationError(AppException):
    """Raised when authentication fails"""

    def __init__(self, message: str = "Authentication failed", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=401, details=details)


class AuthorizationError(AppException):
    """Raised when authorization fails"""

    def __init__(self, message: str = "Not authorized", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=403, details=details)


class NotFoundError(AppException):
    """Raised when a resource is not found"""

    def __init__(self, message: str = "Resource not found", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=404, details=details)


class ValidationError(AppException):
    """Raised when validation fails"""

    def __init__(self, message: str = "Validation error", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=422, details=details)


class ConflictError(AppException):
    """Raised when there's a conflict (e.g., duplicate resource)"""

    def __init__(self, message: str = "Resource conflict", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=409, details=details)


class RateLimitError(AppException):
    """Raised when rate limit is exceeded"""

    def __init__(self, message: str = "Rate limit exceeded", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=429, details=details)


class OpenAIError(AppException):
    """Raised when OpenAI API call fails"""

    def __init__(self, message: str = "OpenAI API error", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=502, details=details)


class DatabaseError(AppException):
    """Raised when database operation fails"""

    def __init__(self, message: str = "Database error", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=500, details=details)


class CacheError(AppException):
    """Raised when cache operation fails"""

    def __init__(self, message: str = "Cache error", details: Optional[Dict[str, Any]] = None):
        super().__init__(message=message, status_code=500, details=details)
