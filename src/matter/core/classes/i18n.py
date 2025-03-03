"""Module that contains i18n implementation"""

from typing import Any

from pyjson5 import loads

from matter import ROOT
from matter.core.classes.config import Config
from matter.core.classes.logger import logger


class Locale(object):
    """Find and operate with locales"""

    # general.locale || {}.locale || *.en_US
    _locale: str = Config().getDict("general", {}).get("locale", "en_US")

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
    """Translate text, return the same text if key is not found

    Args:
        text (str): Text to translate

    Returns:
        str: Translated text
    """
    return _locale.data.get(text, text)
