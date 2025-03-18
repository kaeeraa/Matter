"""Module that contains i18n implementation"""

from typing import Any

from pyjson5 import loads

from matter import ROOT
from matter.core.classes.data import Data
from matter.core.classes.logger import logger


class Locale(object):
    """Find and operate with locales"""

    # general.language || {}.language || *.en_US
    if (_general := Data(isConfig=True).getDict("general", {})) == {}:
        logger.error("General section in config is empty. Using default language.")

    _locale: str = _general.get("language", "en_US")

    data: dict[str, Any] = {}
    _path: str = f"{ROOT}/configuration/lang/{_locale}.json5"

    def __init__(self) -> None:
        try:
            with open(self._path, mode="r", encoding="utf-8") as f:
                self.data = loads(f.read())
        except FileNotFoundError:
            logger.warning("Locale {} not found. Using en_US".format(self._locale))
            self.data = {}


_locale = Locale()


def tr(text: str) -> str:
    """Translate text, return the same text if key is not found"""
    return _locale.data.get(text, text)
