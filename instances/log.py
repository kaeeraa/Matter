"""
This module contains the logging setup logic.

The logging is done using the loguru library. A custom format is used to print
the date and time, log level, module name, function name, line number and log
message. The log format is as follows:

<green>{time:HH:mm:ss:SSS}</green> |
<level>{level.icon} {level} {level.icon}</level> |
<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>

The log level is set to DEBUG if the "-V" or "--verbose" flag is passed on the
command line, otherwise it is set to INFO.

"""

from datetime import datetime
from random import randbytes
from sys import stdout

from loguru import logger

from instances.args import args

# Remove all existing handlers
logger.remove()

# Define custom log levels with associated colors and icons
logger.level("TRACE", color="<white>", icon="🩶 ")
logger.level("DEBUG", color="<magenta>", icon="💜")
logger.level("INFO", color="<green>", icon="💚")
logger.level("SUCCESS", color="<green>", icon="💚")
logger.level("WARNING", color="<yellow>", icon="💛")
logger.level("ERROR", color="<red>", icon="💔")
logger.level("CRITICAL", color="<red>", icon="💔")

if args.verbose:
    LEVEL = "DEBUG"
elif args.vomit:
    LEVEL = "TRACE"
else:
    LEVEL = "INFO"

# Add a file handler with specific configurations
logger.add(
    # Generate a unique log filename ({time}_xxxxxxxx.log)
    sink=f"logs/{datetime.now().strftime('%Y-%m-%d')}_{randbytes(n=4).hex()}.log",
    format="<green>{time:HH:mm:ss:SSS}</green> | "
    "<level>{level}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=LEVEL,  # Set level based on verbosity
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
    "{level.icon} | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level=LEVEL,  # Set level based on verbosity
)
