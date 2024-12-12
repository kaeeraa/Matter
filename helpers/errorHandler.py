"""Contains error handler(s)"""

from arc import GatewayContext

from instances.log import logger


async def sendError(e: Exception, ctx: GatewayContext, cmd: str) -> None:
    """
    Handles any errors that occur in commands by logging the error and sending an error message to the user.

    Args:
        e (Exception): The error that occurred.
        ctx (GatewayContext): The context of the command invocation.
        cmd (str): The name of the command which the error occurred in.
    """
    logger.error(f"Error in {cmd} command: {e}")
    await ctx.respond("An error occurred while processing your request.")
