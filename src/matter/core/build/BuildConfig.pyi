from _typeshed import Incomplete


class BuildConfig:
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def get(cls, key: str) -> str: ...


build: Incomplete
