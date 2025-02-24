"""Module contains implementation and configuration of loguru logger"""

from datetime import datetime
from random import randbytes
from sys import stdout

from loguru import logger

from matter import ROOT
from matter.core.classes.args import args

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

level: str = "INFO"

if args.verbose:
    level = "DEBUG"
if args.vomit:
    level = "TRACE"

# Add a file handler with specific configurations
logger.add(
    # Generate a unique log filename ({time}_xxxxxxxx.log)
    sink=f"{ROOT}/logs/{datetime.now().strftime('%Y-%m-%d')}_{randbytes(n=4).hex()}.log",
    format="<green>{time:HH:mm:ss:SSS}</green> | "
    "<level>{level}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=level,
    # Enable log serialization
    serialize=False,
    # Disable colorization in file logs
    colorize=False,
    # Rotate logs after reaching 10 MB
    rotation="10 MB",
    # Retain logs for 7 days
    retention="7 days",
    # Compress rotated logs using zip
    compression="zip",
    # Enable asynchronous logging
    enqueue=True,
)

# Add a stdout handler for console output
logger.add(
    sink=stdout,
    format="<green>{time:HH:mm:ss:SSS}</green> | "
    "<level>{level.icon}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=level,
    # Enable asynchronous logging
    enqueue=True,
)
