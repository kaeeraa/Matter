"""Module contains implementation and configuration of loguru logger"""

from datetime import datetime
from random import randbytes
from sys import stdout

from loguru import logger

from matter.core.classes.args import args
from matter import ROOT

# Remove all existing handlers
logger.remove()

# Define custom log levels with associated colors and icons
logger.level("TRACE", color="<white>", icon="T")
logger.level("DEBUG", color="<magenta>", icon="D")
logger.level("DEPRECATION", no=15, color="<white>", icon="P")
logger.level("INFO", color="<green>", icon="I")
logger.level("SUCCESS", color="<green>", icon="S")
logger.level("WARNING", color="<yellow>", icon="W")
logger.level("ERROR", color="<red>", icon="E")
logger.level("CRITICAL", color="<red>", icon="C")

# Set log level based on verbosity
match args:
    case {"vomit": True}:
        level = "TRACE"
    case {"verbose": True}:
        level = "DEBUG"
    case _:
        level = "INFO"

# Add a file handler with specific configurations
logger.add(
    # Generate a unique log filename ({time}_xxxxxxxx.log)
    sink=f"{ROOT}/logs/{datetime.now().strftime('%Y-%m-%d')}_{randbytes(n=4).hex()}.log",
    format="<green>{time:HH:mm:ss:SSS}</green> | "
    "<level>{level}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=level,  # Set level based on verbosity
    serialize=False,  # Enable log serialization
    colorize=False,  # Disable colorization in file logs
    rotation="10 MB",  # Rotate logs after reaching 10 MB
    retention="7 days",  # Retain logs for 7 days
    compression="zip",  # Compress rotated logs using zip
    enqueue=True,  # Enable asynchronous logging
)

# Add a stdout handler for console output
logger.add(
    sink=stdout,
    format="<green>{time:HH:mm:ss:SSS}</green> | "
    "<level>{level.icon}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=level,  # Set level based on verbosity
    enqueue=True,  # Enable asynchronous logging
)
