"""
This module handles the configuration settings for the application.

It reads and decodes the configuration from a JSON5 file located in the
configuration directory. The configuration is loaded into a dictionary
object for use throughout the application.
"""

from typing import Any, TypeVar

from pyjson5 import loads

from matter import ROOT
from matter.core.classes.logger import logger

T = TypeVar("T", str, dict[str, Any], bool, int)


class Config(object):
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

    def __init__(self) -> None:
        self._config = self._load(self._path)

    @staticmethod
    def _load(path: str = _path) -> dict[str, Any]:
        with open(file=path, mode="r", encoding="utf-8") as f:
            return loads(f.read())

    def _get(self, key: str, default: T) -> T:
        value: Any | None = self._config.get(key)

        if not isinstance(value, type(default)):
            logger.error(
                "Key '%s' has invalid type (excepted %s, got %s). Using default.",
                key,
                type(default).__name__,
                type(value).__name__,
            )
            return default

        # type(value) == T
        return value

    def getStr(self, key: str, default: str) -> str:
        return self._get(key, default)

    def getDict(self, key: str, default: dict[str, Any]) -> dict[str, Any]:
        return self._get(key, default)

    def getBool(self, key: str, default: bool) -> bool:
        return self._get(key, default)

    def getInt(self, key: str, default: int) -> int:
        return self._get(key, default)
