from arc import GatewayContext as GatewayContext
from typing import Annotated

COMMAND_NAME: str
COMMAND_DESCRIPTION: str

async def newTicket(
    ctx: GatewayContext, title: Annotated[str, str] = "Ndfined", description: Annotated[str, str] = "None"
) -> None: ...
