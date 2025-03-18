"""
This module contains the data class, which is responsible for reading and
providing access to data stored in JSON5 files.

The data class reads the data from JSON5 files located in the data
directory and loads it into a dictionary object. It offers methods to
retrieve specific data associated with a given key.

"""

from os.path import exists
from pathlib import Path
from typing import Any, Optional, TypeVar

from pyjson5 import Json5EOF, decode, encode, loads

from matter import ROOT
from matter.core.classes.logger import logger

T = TypeVar("T", str, dict[str, Any], bool, int)


class Data(object):
    """Load and manipulate the data"""

    _partition: str
    _data: dict[str, Any] = {}
    _path: str

    def __init__(self, partition: str = "", isConfig: bool = False) -> None:
        if isConfig:
            self._path: str = f"{ROOT}/configuration/settings.json5"
        else:
            if partition == "":
                logger.error("'partition' param is not specified")
                return

            self._partition = partition
            self._path = f"{ROOT}/data/{self._partition}.json5"

        if not exists(self._path):
            logger.warning(f"File {self._path} is not exists. Creating.")
            Path(self._path).touch()

        with open(self._path, mode="r", encoding="utf-8") as f:
            try:
                current: dict[str, Any] = loads(f.read())
                self._data = current
            except Json5EOF:
                # silently fix EOF
                # write {} into file
                self._data = {}
                self._write()

    def _write(self) -> None:
        with open(file=self._path, mode="w", encoding="utf-8") as f:
            f.write(encode(self._data))

    def _get(self, key: str, default: T) -> T:
        dicts: list[str] = key.split(".")
        value: Optional[Any] = self._data

        for key_ in dicts:
            if not value:
                break

            value = value.get(key_, None)

        if not isinstance(value, type(default)):
            logger.error(
                "Key '{}' has invalid type (excepted {}, got {}). Using default.",
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

    def put(self, path: str, data: dict[str, Any]) -> None:
        try:
            decode(encode(data))
        except RecursionError:
            logger.error("Data contains circular reference")
            return

        _parts: list[str] = path.split(".")
        _current: dict[str, Any] = self._data

        for part in _parts[:-1]:
            if part not in _current or not isinstance(_current[part], dict):
                _current[part] = {}
            _current = _current[part]

        _last_part: str = _parts[-1]
        _current[_last_part] = data

        self._write()

    def remove(self, path: str) -> None:
        self._data.pop(path)
        self._write()
