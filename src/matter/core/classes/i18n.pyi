from typing import Any

class Locale(object):
    data: dict[str, Any]
    def __init__(self) -> None: ...

def tr(text: str) -> str: ...
