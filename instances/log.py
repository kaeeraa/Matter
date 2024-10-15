from loguru import logger
from sys import argv, stdout
from random import randbytes
from datetime import datetime

# Remove all existing handlers
logger.remove()

# Define custom log levels with associated colors and icons
logger.level("TRACE", color="<white>", icon="🩶")
logger.level("DEBUG", color="<magenta>", icon="💜")
logger.level("INFO", color="<green>", icon="💚")
logger.level("SUCCESS", color="<green>", icon="💚")
logger.level("WARNING", color="<yellow>", icon="💛")
logger.level("ERROR", color="<red>", icon="💔")
logger.level("CRITICAL", color="<red>", icon="💔")
# Add a file handler with specific configurations
logger.add(
    sink=f"logs/{datetime.now().strftime('%Y-%m-%d')}_{randbytes(n=4).hex()}.log",
    format="<green>{time:HH:mm:ss:SSS}</green> | "
    "<level>{level}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=(
        "TRACE" if any(arg in ["-V", "--verbose"] for arg in argv) else "DEBUG"
    ),  # Set level based on verbosity
    serialize=True,  # Enable log serialization
    colorize=False,  # Disable colorization in file logs
    rotation="10 MB",  # Rotate logs after reaching 10 MB
    retention="7 days",  # Retain logs for 7 days
    compression="zip",  # Compress rotated logs using zip
)

# Add a stdout handler for console output
logger.add(
    sink=stdout,
    format="<green>{time:HH:mm:ss:SSS}</green> | "
    "<level>{level}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=(
        "TRACE" if any(arg in ["-V", "--verbose"] for arg in argv) else "DEBUG"
    ),  # Set level based on verbosity
)
