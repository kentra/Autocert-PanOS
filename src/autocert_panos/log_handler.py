from loguru import logger
import sys

# Remove all handlers added so far, including the default one.
logger.remove()
# logger.add("logs/log_handler.log", rotation="10 MB", retention="10 days", level="DEBUG")
# logger.add(sys.stdout, colorize=True, format="{time} {level} {message}", level="DEBUG")
logger.add(sys.stdout, colorize=True, level="DEBUG")
