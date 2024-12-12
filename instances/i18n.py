"""
    This module contains the Locale class, which is used to provide localization support for the bot.
"""

from io import StringIO

# IDK why pylint doesn't like this | pylint: disable=no-name-in-module
from pyjson5 import decode_io

from root import rootDir


class Locale:
    """
    A class representing a locale.

    The Locale class provides methods for setting and retrieving strings from a
    specified locale. It is used to provide localization support for the bot.

    Attributes:
        locale (str): The default locale, initially set to "en_US".
        data (dict): A dictionary containing the language data for the current locale.
    """

    def __init__(self):
        """
        Initializes a new Locale instance with the default locale set to "en_US".
        Loads the language data from the corresponding JSON5 file into the instance.

        Attributes:
            locale (str): The default locale, initially set to "en_US".
            data (dict): A dictionary containing the language data for the current locale.
        """
        self.locale = "en_US"

        with open(f"{rootDir}/configuration/lang/{self.locale}.json5", "r", encoding="utf-8") as f:
            self.data = decode_io(StringIO(f.read()))

    def setLocale(self, locale: str):
        """
        Sets the locale to the specified locale and reloads the associated language file.

        Args:
            locale (str): The locale to set.
        """
        self.locale = locale

        with open(f"{rootDir}/configuration/lang/{self.locale}.json5", "r", encoding="utf-8") as f:
            self.data = decode_io(StringIO(f.read()))

    def getString(self, key: str) -> str:
        """
        Returns the string associated with a given key from the currently set locale.

        Args:
            key (str): The key to retrieve the string for.

        Returns:
            str: The string associated with the given key.
        """
        return self.data[key]

    def getLocale(self) -> str:
        """
        Returns the currently set locale.

        Returns:
            str: The current locale as a string.
        """
        return self.locale

    def getPath(self) -> str:
        """
        Returns the path to the language file for the currently set locale.

        Returns:
            str: The path to the language file.
        """
        return f"{rootDir}/configuration/lang/{self.locale}.json5"
