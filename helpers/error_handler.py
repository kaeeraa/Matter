"""Contains error handler(s)"""

from instances.log import logger
from arc import GatewayContext


async def send_error(e: Exception, ctx: GatewayContext, cmd: str) -> None:
    logger.error(f"Error in {cmd} command: {e}")
    await ctx.respond("An error occurred while processing your request.")
