"""
This module contains the data class, which is responsible for reading and
providing access to data stored in JSON5 files.

The data class reads the data from JSON5 files located in the data
directory and loads it into a dictionary object. It offers methods to
retrieve specific data associated with a given key.

"""

from pathlib import Path
from typing import Any

from pyjson5 import Json5EOF, decode, encode, loads

from matter import ROOT
from matter.core.classes.i18n import tr
from matter.core.classes.logger import logger


class Data(object):
    """Load and manipulate the data"""

    _partition: str
    _data: dict[str, Any]
    _path: str

    def __init__(self, partition: str) -> None:
        self._partition = partition
        self._path = f"{ROOT}/data/{self._partition}.json5"

        with open(file=self._path, mode="r", encoding="utf-8") as f:
            try:
                self._data = loads(f.read())
            except Json5EOF:
                self._data = {}
            except FileNotFoundError:
                Path(self._path).touch()

    def _write(self) -> None:
        with open(file=self._path, mode="w", encoding="utf-8") as f:
            f.write(encode(self._data))

    @logger.catch(level="ERROR", message=tr("Failed to read data"))
    def get(self, path: str, default: Any | None = None) -> Any | None:
        return self._data.get(path, default)

    @logger.catch(level="ERROR", message=tr("Failed to write data"))
    def put(self, path: str, data: dict[str, Any]) -> None:
        try:
            decode(encode(data))
        except RecursionError:
            logger.error(tr("Data contains circular reference"))
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

    @logger.catch(level="ERROR", message=tr("Failed to remove data"))
    def remove(self, path: str) -> None:
        self._data.pop(path)
        self._write()
