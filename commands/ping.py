"""
A simple ping command that returns the bot's heartbeat latency.

Example:
    /ping
"""

from json import load
from urllib.error import URLError
from urllib.request import urlopen

from arc import GatewayContext, slash_command

from helpers.embed import new_embed
from instances.bot import bot
from instances.log import logger

logger.trace("Initialising ping command")

try:
    with urlopen("https://worldtimeapi.org/api/timezone", timeout=5) as f:
        data: dict = load(f)
except URLError:
    logger.error("Failed to get server geo data")
    data = {
        "country": "Unknown",
        "region": "Unknown",
    }


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
    embed = new_embed(
        ctx,
        title="🏓 Network details",
        description=(
            f"- 🌍 Server Geo: {data['country']}, {data['region']}\n"
            f"- ⏳ Latency: {round(bot.heartbeat_latency * 1000)}ms "
        ),
    )
    await ctx.respond(embed=embed)
