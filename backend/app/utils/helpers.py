"""
Helper Utility Functions
Common utility functions used across the application
"""

import re
from typing import Any, Dict, Optional
from datetime import datetime, timezone


def generate_conversation_title(message: str, max_length: int = 60) -> str:
    """
    Generate a conversation title from a message.

    Args:
        message: Message content
        max_length: Maximum title length

    Returns:
        Generated title string

    Example:
        >>> generate_conversation_title("Hello, how are you today?")
        'Hello, how are you today?'
        >>> generate_conversation_title("A" * 100, max_length=50)
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA...'
    """
    # Remove extra whitespace
    clean_message = re.sub(r'\s+', ' ', message.strip())

    # Truncate if too long
    if len(clean_message) > max_length:
        return clean_message[:max_length].strip() + "..."

    return clean_message


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """
    Format datetime to ISO 8601 string with UTC timezone.

    Args:
        dt: Datetime object (uses current time if None)

    Returns:
        ISO formatted datetime string

    Example:
        >>> format_timestamp()
        '2025-01-01T12:00:00.000Z'
    """
    if dt is None:
        dt = datetime.now(timezone.utc)

    return dt.isoformat()


def sanitize_string(text: str, max_length: Optional[int] = None) -> str:
    """
    Sanitize string by removing dangerous characters and limiting length.

    Args:
        text: Text to sanitize
        max_length: Maximum length (no limit if None)

    Returns:
        Sanitized string

    Example:
        >>> sanitize_string("<script>alert('xss')</script>")
        'scriptalert(xss)/script'
    """
    # Remove HTML/XML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove control characters except newlines and tabs
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)

    # Trim whitespace
    text = text.strip()

    # Limit length if specified
    if max_length and len(text) > max_length:
        text = text[:max_length]

    return text


def extract_error_message(exception: Exception) -> str:
    """
    Extract a user-friendly error message from an exception.

    Args:
        exception: Exception object

    Returns:
        Error message string

    Example:
        >>> try:
        ...     raise ValueError("Invalid input")
        ... except Exception as e:
        ...     msg = extract_error_message(e)
    """
    error_msg = str(exception)

    # Remove sensitive information patterns
    error_msg = re.sub(r'password[=:]\s*\S+', 'password=***', error_msg, flags=re.IGNORECASE)
    error_msg = re.sub(r'token[=:]\s*\S+', 'token=***', error_msg, flags=re.IGNORECASE)
    error_msg = re.sub(r'key[=:]\s*\S+', 'key=***', error_msg, flags=re.IGNORECASE)

    return error_msg


def paginate_results(
    items: list,
    page: int = 1,
    page_size: int = 20
) -> Dict[str, Any]:
    """
    Paginate a list of items.

    Args:
        items: List of items to paginate
        page: Page number (1-indexed)
        page_size: Number of items per page

    Returns:
        Dictionary with pagination metadata and items

    Example:
        >>> items = list(range(100))
        >>> result = paginate_results(items, page=2, page_size=10)
        >>> result['page']
        2
        >>> len(result['items'])
        10
    """
    total = len(items)
    total_pages = (total + page_size - 1) // page_size

    # Validate page number
    if page < 1:
        page = 1
    if page > total_pages and total_pages > 0:
        page = total_pages

    # Calculate slice indices
    start = (page - 1) * page_size
    end = start + page_size

    return {
        "items": items[start:end],
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }


def is_valid_uuid(uuid_string: str) -> bool:
    """
    Check if string is a valid UUID.

    Args:
        uuid_string: String to validate

    Returns:
        True if valid UUID, False otherwise

    Example:
        >>> is_valid_uuid("123e4567-e89b-12d3-a456-426614174000")
        True
        >>> is_valid_uuid("not-a-uuid")
        False
    """
    uuid_pattern = re.compile(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        re.IGNORECASE
    )
    return bool(uuid_pattern.match(uuid_string))


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to maximum length, adding suffix if truncated.

    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated

    Returns:
        Truncated text

    Example:
        >>> truncate_text("This is a very long text", max_length=10)
        'This is...'
    """
    if len(text) <= max_length:
        return text

    return text[:max_length - len(suffix)].strip() + suffix
