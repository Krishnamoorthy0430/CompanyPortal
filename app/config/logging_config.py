import logging
import colorlog


def setup_logging(level: str = "INFO") -> None:
    """Configure colorful logging for the application.

    Uses different colors for different log levels:
    - DEBUG: Blue
    - INFO: Green
    - WARNING: Yellow
    - ERROR: Red
    - CRITICAL: Red (Bold)
    """
    # Create color handler
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s | %(levelname)-7s | %(name)s | %(message)s%(reset)s",
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bold',
        },
        secondary_log_colors={},
        style='%'
    ))

    # Get root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    
    # Remove any existing handlers and add color handler
    root_logger.handlers = []
    root_logger.addHandler(handler)

    # Allow standard uvicorn startup messages but reduce access log noise
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)  # Reduce HTTP access logs
    logging.getLogger("uvicorn.error").setLevel(logging.INFO)      # Show startup messages

