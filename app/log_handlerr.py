from loguru import logger

logger.add("logs/log_handler.log", rotation="10 MB", retention="10 days", level="DEBUG")
