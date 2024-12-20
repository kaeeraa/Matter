"""
This module handles the configuration settings for the application.

It reads and decodes the configuration from a JSON5 file located in the
configuration directory. The configuration is loaded into a dictionary
object for use throughout the application.
"""

from io import StringIO

# IDK why pylint doesn't like this | pylint: disable=no-name-in-module
from pyjson5 import decode_io

from root import rootDir


class Config:
    """
    The Config class is responsible for loading and providing access to
    configuration settings for the application.

    This class reads the configuration from a JSON5 file located in the
    configuration directory and loads it into a dictionary object. It
    offers methods to retrieve specific configuration values such as the
    bot token and owner.

    Attributes:
        config (dict): A dictionary containing the configuration settings
        loaded from the JSON5 file.
    """

    def __init__(self):
        with open(f"{rootDir}/configuration/settings.json5", "r", encoding="utf-8") as f:
            self.config = decode_io(StringIO(f.read()))

    def getToken(self) -> str:
        """
        Returns the bot token.

        Returns:
            str: The bot token.
        """
        return self.config["bot"]["token"]

    def getOwner(self) -> int:
        """
        Returns the owner of the bot.

        Returns:
            int: The owner of the bot.
        """
        return self.config["bot"]["owner"]

    def getConfig(self) -> dict:
        """
        Returns the keys of the bot.

        Returns:
            list: The keys of the bot.
        """
        return self.config
