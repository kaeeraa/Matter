from arc import GatewayContext as GatewayContext
from matter.core.classes.bot import bot as bot
from matter.core.classes.i18n import tr as tr
from matter.core.classes.logger import logger as logger
from matter.core.helpers.embed import embed as embed
from typing import Any

COMMAND_NAME: str
COMMAND_DESCRIPTION: str
data: dict[str, Any]

async def ping(ctx: GatewayContext) -> None: ...
