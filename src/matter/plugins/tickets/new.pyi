from typing import Annotated

from arc import GatewayContext as GatewayContext, StrParams

COMMAND_NAME: str
COMMAND_DESCRIPTION: str

async def new(ctx: GatewayContext, topic: Annotated[str, StrParams]) -> None: ...
