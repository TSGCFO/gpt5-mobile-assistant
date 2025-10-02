"""
Logging Configuration
Structured JSON logging for production environments
"""

import logging
import sys
from pythonjsonlogger import jsonlogger
from app.core.config import settings


def setup_logging():
    """
    Configure application logging with JSON formatter.

    Logs include:
    - timestamp
    - log level
    - message
    - module/function name
    - additional context fields
    """
    # Create JSON formatter
    log_format = "%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s"
    json_formatter = jsonlogger.JsonFormatter(log_format)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))

    # Remove existing handlers
    root_logger.handlers.clear()

    # Add console handler with JSON formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(json_formatter)
    root_logger.addHandler(console_handler)

    # Set specific log levels for libraries
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.INFO)

    return root_logger


# Create logger instance
logger = setup_logging()


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for a specific module.

    Args:
        name: Logger name (typically __name__ of the module)

    Returns:
        Logger instance

    Example:
        logger = get_logger(__name__)
        logger.info("Processing request", extra={"user_id": "123"})
    """
    return logging.getLogger(name)
