from typing import Any
from tomli import loads
from matter.core.classes.exceptions import ProjectConfigurationNotFound
from matter.core.classes.logger import logger
from matter import PROJECT_ROOT


class BuildConfig:
    _config: dict[str, Any] = {}
    _content: str = ""

    try:
        with open(f"{PROJECT_ROOT}/pyproject.toml", "r", encoding="utf-8") as f:
            _content = f.read()
        _config = loads(_content).get("tool", {}).get("poetry", {})
    except FileNotFoundError:
        raise ProjectConfigurationNotFound

    def __init_subclass__(cls) -> None:
        for key, value in cls._config.items():
            setattr(cls, key.upper(), value)

    @classmethod
    def get(cls, key: str) -> str:
        value: str = cls._config.get(key, "")

        if value == "":
            logger.error("Key '{}' is undefined", key)

        return value


build = BuildConfig()
