from arc import GatewayContext as GatewayContext
from typing import Any

COMMAND_NAME: str
COMMAND_DESCRIPTION: str
data: dict[str, Any]


async def ping(ctx: GatewayContext) -> None: ...
