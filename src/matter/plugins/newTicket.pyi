from arc import GatewayContext as GatewayContext
from arc import Option

COMMAND_NAME: str
COMMAND_DESCRIPTION: str

async def newTicket(
    ctx: GatewayContext, title: Option[str, str] = "Ndfined", description: Option[str, str] = "None"
) -> None: ...
