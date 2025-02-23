"""
This module handles the configuration settings for the application.

It reads and decodes the configuration from a JSON5 file located in the
configuration directory. The configuration is loaded into a dictionary
object for use throughout the application.
"""

from typing import Any

from pyjson5 import loads

from matter import ROOT
from matter.core.classes.logger import logger


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

    _config: dict[str, Any] = {}
    _path: str = f"{ROOT}/configuration/settings.json5"

    def __init__(self):
        self._config = self._load(self._path)

    def _load(self, path: str = _path) -> dict[str, Any]:
        with open(path, "r", encoding="utf-8") as f:
            return loads(f.read())

    def getString(self, key: str) -> str:
        value: str = self._config.get(key, "")

        if value == "":
            logger.error("Key '{}' is undefined", key)

        return value

    def getDictionary(self, key: str) -> dict[str, Any]:
        value: dict[str, Any] = self._config.get(key, {})

        if value == {}:
            logger.error("Key '{}' is undefined", key)

        return value
