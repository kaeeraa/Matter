from typing import Any

from arc import GatewayContext as GatewayContext

COMMAND_NAME: str
COMMAND_DESCRIPTION: str
data: dict[str, Any]

async def ping(ctx: GatewayContext) -> None: ...
