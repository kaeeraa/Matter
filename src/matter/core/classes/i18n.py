"""Module that contains i18n implementation"""

from typing import Any

from pyjson5 import loads

from matter import ROOT


class Locale:
    """A Locale i18n class

    Returns:
        str: as described in methods
    """

    _locale: str = "en_US"
    _data: dict[str, Any]
    _path: str = f"{ROOT}/configuration/lang/{_locale}.json5"

    def __init__(self):
        """Init Locale class with _locale"""

        with open(self._path, "r", encoding="utf-8") as f:
            self._data = loads(f.read())

    def setLocale(self, locale: str):
        """Change locale file

        Args:
            locale (str): locale file name
        """
        self._locale = locale
        self._path = f"/configuration/lang/{locale}.json5"

        with open(f"/configuration/lang/{locale}.json5", "r", encoding="utf-8") as f:
            self._data = loads(f.read())

    def get(self, key: str) -> str:
        """Get key value in current locale

        Args:
            key (str): an key

        Returns:
            str: if key exists return non-empty str
        """
        return self._data.get(key, "")

    def current(self) -> str:
        """Get current locale

        Returns:
            str: name of current locale
        """
        return self._locale

    def path(self) -> str:
        """Get path to current locale

        Returns:
            str: path to locale
        """
        return f"/configuration/lang/{self._locale}.json5"
