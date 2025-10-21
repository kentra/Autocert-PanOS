from loguru import logger


# Remove all handlers added so far, including the default one.
logger.remove()
logger.add("logs/log_handler.log", rotation="10 MB", retention="10 days", level="DEBUG")
