"""
Rate Limiting Middleware
Prevent API abuse by limiting requests per user
"""

import time
from typing import Optional
from fastapi import Request, HTTPException, status
from app.utils.cache import RedisCache, get_cache
from app.models.user import User
from app.core.config import settings
from app.core.logging_config import get_logger

logger = get_logger(__name__)


class RateLimiter:
    """
    Rate limiter using Redis for distributed rate limiting.

    Features:
    - Per-user rate limiting
    - Sliding window algorithm
    - Configurable limits
    """

    def __init__(self, cache: RedisCache):
        """
        Initialize rate limiter.

        Args:
            cache: Redis cache instance
        """
        self.cache = cache
        self.default_limit = settings.RATE_LIMIT_PER_MINUTE
        self.window_seconds = 60  # 1 minute window

    async def check_rate_limit(
        self,
        user_id: str,
        limit: Optional[int] = None
    ) -> tuple[bool, int]:
        """
        Check if user has exceeded rate limit.

        Args:
            user_id: User identifier
            limit: Custom limit (uses default if None)

        Returns:
            Tuple of (is_allowed, remaining_requests)

        Example:
            >>> is_allowed, remaining = await limiter.check_rate_limit(user_id)
            >>> if not is_allowed:
            ...     raise HTTPException(status_code=429)
        """
        try:
            rate_limit = limit or self.default_limit
            key = f"rate_limit:{user_id}"

            # Get current count
            current = await self.cache.get(key)

            if current is None:
                # First request in window
                await self.cache.set(key, 1, ttl=self.window_seconds)
                remaining = rate_limit - 1
                logger.debug(f"Rate limit initialized for user {user_id}: {remaining} remaining")
                return True, remaining

            current_count = int(current)

            if current_count >= rate_limit:
                # Rate limit exceeded
                logger.warning(f"Rate limit exceeded for user {user_id}")
                return False, 0

            # Increment counter
            new_count = await self.cache.increment(key)
            remaining = rate_limit - new_count

            logger.debug(f"Rate limit check for user {user_id}: {remaining} remaining")
            return True, remaining

        except Exception as e:
            logger.error(f"Rate limit check error: {str(e)}")
            # Fail open - allow request on error
            return True, rate_limit

    async def reset_rate_limit(self, user_id: str):
        """
        Reset rate limit for a user.

        Args:
            user_id: User identifier
        """
        key = f"rate_limit:{user_id}"
        await self.cache.delete(key)
        logger.info(f"Rate limit reset for user {user_id}")


async def rate_limit_dependency(
    request: Request,
    user: User,
    cache: RedisCache = get_cache()
):
    """
    FastAPI dependency for rate limiting.
    Raises HTTPException if rate limit is exceeded.

    Args:
        request: FastAPI request object
        user: Current authenticated user
        cache: Redis cache instance

    Raises:
        HTTPException: 429 if rate limit exceeded

    Usage:
        @app.get("/api/data", dependencies=[Depends(rate_limit_dependency)])
        def get_data(user: User = Depends(get_current_user)):
            return {"data": "..."}
    """
    limiter = RateLimiter(cache)
    is_allowed, remaining = await limiter.check_rate_limit(str(user.id))

    # Add rate limit headers to response
    request.state.rate_limit_remaining = remaining

    if not is_allowed:
        logger.warning(f"Rate limit exceeded for user {user.username} ({user.id})")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please try again later.",
            headers={
                "Retry-After": "60",
                "X-RateLimit-Limit": str(settings.RATE_LIMIT_PER_MINUTE),
                "X-RateLimit-Remaining": "0",
            }
        )


def get_rate_limiter(cache: RedisCache = get_cache()) -> RateLimiter:
    """
    Get rate limiter instance.
    Use as FastAPI dependency for manual rate limiting.

    Example:
        @app.post("/api/heavy-operation")
        async def heavy_op(
            user: User = Depends(get_current_user),
            limiter: RateLimiter = Depends(get_rate_limiter)
        ):
            is_allowed, remaining = await limiter.check_rate_limit(str(user.id), limit=10)
            if not is_allowed:
                raise HTTPException(status_code=429)
            # ... perform operation
    """
    return RateLimiter(cache)
