"""
Security Utilities
Password hashing and verification using bcrypt_sha256

bcrypt_sha256 eliminates the 72-byte password limitation by pre-hashing
passwords with HMAC-SHA256 before applying bcrypt. This is the official
PassLib-recommended solution for handling long passwords.

See: Docs/passlib/lib/passlib.hash.bcrypt_sha256.md
"""

from passlib.context import CryptContext


# Configure password context with bcrypt_sha256
# This eliminates the 72-byte password limit by pre-hashing with HMAC-SHA256
pwd_context = CryptContext(
    schemes=["bcrypt_sha256"],
    deprecated="auto",
    bcrypt_sha256__rounds=12  # PassLib default; targets ~300ms per hash
)


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt_sha256.

    bcrypt_sha256 pre-hashes the password with HMAC-SHA256 before applying bcrypt,
    eliminating the 72-byte limitation and providing enhanced security.

    Args:
        password: Plain text password to hash (any length supported)

    Returns:
        Hashed password string in bcrypt_sha256 format

    Example:
        >>> hashed = hash_password("mysecretpassword")
        >>> print(hashed)
        $bcrypt-sha256$v=2,t=2b,r=12$... (varies based on salt)

    See Also:
        Docs/passlib/lib/passlib.hash.bcrypt_sha256.md - bcrypt_sha256 documentation
        Docs/passlib/lib/passlib.hash.bcrypt.md - Why bcrypt_sha256 is recommended
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain text password against its hash.

    Uses bcrypt_sha256 which supports passwords of any length.

    Args:
        plain_password: Plain text password to verify (any length supported)
        hashed_password: Hashed password to verify against

    Returns:
        True if password matches, False otherwise

    Example:
        >>> hashed = hash_password("mysecretpassword")
        >>> verify_password("mysecretpassword", hashed)
        True
        >>> verify_password("wrongpassword", hashed)
        False

    See Also:
        Docs/passlib/lib/passlib.hash.bcrypt_sha256.md
    """
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        # Handle any verification errors (invalid hash format, etc.)
        return False


def is_password_strong(password: str) -> tuple[bool, str]:
    """
    Check if a password meets strength requirements.

    Requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit

    Note:
        bcrypt_sha256 supports passwords of any length, so no maximum limit is enforced.
        A reasonable maximum (e.g., 128 characters) could be added to prevent abuse.

    Args:
        password: Password to check

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_password_strong("Weak1")
        (False, "Password must be at least 8 characters long")
        >>> is_password_strong("Strong1Password")
        (True, "")
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    # Optional: Add reasonable maximum to prevent abuse
    if len(password) > 128:
        return False, "Password must be 128 characters or less"

    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"

    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"

    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit"

    return True, ""
