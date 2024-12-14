"""
A simple ping command that returns the bot's heartbeat latency.

Example:
    /ping
"""

from json import load
from urllib.error import URLError
from urllib.request import urlopen

from arc import GatewayContext, slash_command

from helpers.errorHandler import sendError
from helpers.embed import newEmbed

from instances.bot import bot
from instances.log import logger

COMMAND_NAME = "ping"
COMMAND_DESCRIPTION = "Returns the bot's heartbeat latency."

logger.trace("Initializing ping command")

data: dict = {}

try:
    with urlopen("http://ip-api.com/json/?fields=country,regionName,city", timeout=5) as f:
        data = load(f)
except URLError:  # it can be unavailable btw
    logger.error("Failed to get server geo data")


@slash_command(name="ping", description="Returns the bot's heartbeat latency.")
async def ping(ctx: GatewayContext) -> None:
    """
    Returns the bot's heartbeat latency.

    Args:
        ctx (GatewayContext): The context that invoked this command.

    Returns:
        None
    """
    logger.trace(f"/ping command called ({ctx.author.username})")

    try:
        country = data.get("country", "Unknown")
        region = data.get("city", "Unknown")
        latency = round(bot.heartbeat_latency * 1000) if bot.heartbeat_latency else "Unavailable"

        await ctx.respond(
            embed=newEmbed(
                ctx.author,
                title="🏓 Network details",
                description=(f"- 🌍 Server Geo: {country}, {region}\n" f"- ⏳ Latency: {latency}ms"),
            )
        )
    except (ValueError, TypeError) as e:
        await sendError(e, ctx, COMMAND_NAME)
