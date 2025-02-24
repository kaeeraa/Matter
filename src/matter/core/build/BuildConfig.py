"""Generate build constants from project configuration

Raises:
    ProjectConfigurationNotFound: Raised if no pyproject.toml is found

Returns:
    str: Return generated constant
"""
from typing import Any
from tomli import loads
from matter.core.classes.exceptions import ProjectConfigurationNotFound
from matter.core.classes.logger import logger
from matter import PROJECT_ROOT


class BuildConfig(object):
    """
    Raises:
        ProjectConfigurationNotFound: Raised if no pyproject.toml is found

    Returns:
        str: Return generated constant
    """
    _config: dict[str, Any] = {}
    _content: str = ""

    try:
        with open(file=f"{PROJECT_ROOT}/pyproject.toml", mode="r", encoding="utf-8") as f:
            _content = f.read()
        _config = loads(_content).get("tool", {}).get("poetry", {})
    except FileNotFoundError:
        raise ProjectConfigurationNotFound

    def __init_subclass__(cls: type[Any]) -> None:
        for key, value in cls._config.items():
            setattr(cls, key.upper(), value)

    @classmethod
    def get(cls, key: str) -> str:
        value: str = cls._config.get(key, "")

        if value == "":
            logger.error("Key '{}' is undefined", key)

        return value


build = BuildConfig()
