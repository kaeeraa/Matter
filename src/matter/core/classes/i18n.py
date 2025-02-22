"""Module that contains i18n implementation"""

from typing import Any

from pyjson5 import loads

from matter import ROOT
from matter.core.classes.config import Config


class Locale:
    _locale: str = Config().getDictionary("general")["language"]
    data: dict[str, Any] = {}
    _path: str = f"{ROOT}/configuration/lang/{_locale}.json5"

    def __init__(self):
        with open(self._path, "r", encoding="utf-8") as f:
            self.data = loads(f.read())


_locale = Locale()


def tr(text: str) -> str:
    return _locale.data.get(text, text)
