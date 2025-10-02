"""
Redis Cache Utilities
Helper functions for Redis caching operations
"""

import json
from typing import Any, Optional
import redis.asyncio as redis
from app.core.config import settings
from app.core.logging_config import get_logger
from app.core.exceptions import CacheError

logger = get_logger(__name__)


class RedisCache:
    """
    Redis cache manager for application-wide caching.

    Features:
    - Async Redis operations
    - JSON serialization
    - TTL management
    - Error handling
    """

    def __init__(self):
        """Initialize Redis connection"""
        self.redis_url = settings.REDIS_URL
        self.default_ttl = settings.REDIS_CACHE_TTL
        self._client: Optional[redis.Redis] = None
        logger.info(f"Redis cache initialized with URL: {self.redis_url}")

    async def get_client(self) -> redis.Redis:
        """Get or create Redis client"""
        if self._client is None:
            self._client = await redis.from_url(
                self.redis_url,
                encoding="utf-8",
                decode_responses=True
            )
        return self._client

    async def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache.

        Args:
            key: Cache key

        Returns:
            Cached value (deserialized from JSON) or None if not found
        """
        try:
            client = await self.get_client()
            value = await client.get(key)

            if value is not None:
                logger.debug(f"Cache hit: {key}")
                return json.loads(value)

            logger.debug(f"Cache miss: {key}")
            return None

        except Exception as e:
            logger.error(f"Cache get error for key {key}: {str(e)}")
            return None

    async def set(
        self,
        key: str,
        value: Any,
        ttl: Optional[int] = None
    ) -> bool:
        """
        Set value in cache with optional TTL.

        Args:
            key: Cache key
            value: Value to cache (will be JSON serialized)
            ttl: Time to live in seconds (uses default if not specified)

        Returns:
            True if successful, False otherwise
        """
        try:
            client = await self.get_client()
            serialized = json.dumps(value)
            ttl_seconds = ttl if ttl is not None else self.default_ttl

            await client.setex(key, ttl_seconds, serialized)
            logger.debug(f"Cache set: {key} (TTL: {ttl_seconds}s)")
            return True

        except Exception as e:
            logger.error(f"Cache set error for key {key}: {str(e)}")
            return False

    async def delete(self, key: str) -> bool:
        """
        Delete value from cache.

        Args:
            key: Cache key to delete

        Returns:
            True if deleted, False otherwise
        """
        try:
            client = await self.get_client()
            result = await client.delete(key)
            logger.debug(f"Cache delete: {key} (existed: {result > 0})")
            return result > 0

        except Exception as e:
            logger.error(f"Cache delete error for key {key}: {str(e)}")
            return False

    async def exists(self, key: str) -> bool:
        """
        Check if key exists in cache.

        Args:
            key: Cache key

        Returns:
            True if exists, False otherwise
        """
        try:
            client = await self.get_client()
            result = await client.exists(key)
            return result > 0

        except Exception as e:
            logger.error(f"Cache exists error for key {key}: {str(e)}")
            return False

    async def increment(self, key: str, amount: int = 1) -> Optional[int]:
        """
        Increment a counter in cache.

        Args:
            key: Cache key
            amount: Amount to increment by

        Returns:
            New value after increment, or None on error
        """
        try:
            client = await self.get_client()
            result = await client.incrby(key, amount)
            logger.debug(f"Cache increment: {key} by {amount} = {result}")
            return result

        except Exception as e:
            logger.error(f"Cache increment error for key {key}: {str(e)}")
            return None

    async def set_with_expiry(
        self,
        key: str,
        value: Any,
        expire_at: int
    ) -> bool:
        """
        Set value with absolute expiration time.

        Args:
            key: Cache key
            value: Value to cache
            expire_at: Unix timestamp when key should expire

        Returns:
            True if successful, False otherwise
        """
        try:
            client = await self.get_client()
            serialized = json.dumps(value)

            await client.set(key, serialized)
            await client.expireat(key, expire_at)

            logger.debug(f"Cache set with expiry: {key} at {expire_at}")
            return True

        except Exception as e:
            logger.error(f"Cache set_with_expiry error for key {key}: {str(e)}")
            return False

    async def close(self):
        """Close Redis connection"""
        if self._client:
            await self._client.close()
            logger.info("Redis connection closed")


# Global cache instance
_cache: Optional[RedisCache] = None


def get_cache() -> RedisCache:
    """
    Get or create Redis cache instance.
    Use as FastAPI dependency.

    Example:
        @app.get("/data")
        async def get_data(cache: RedisCache = Depends(get_cache)):
            cached = await cache.get("my_key")
            return cached
    """
    global _cache
    if _cache is None:
        _cache = RedisCache()
    return _cache
