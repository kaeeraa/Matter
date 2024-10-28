"""
A simple ping command that returns the bot's heartbeat latency.

Example:
    /ping
"""

from datetime import datetime
from json import load
from urllib.error import URLError
from urllib.request import urlopen

from arc import GatewayContext, slash_command
from hikari import Color
from hikari.embeds import Embed

from instances.bot import bot
from instances.log import logger

logger.trace("Initialising ping command")

try:
    with urlopen("https://worldtimeapi.org/api/timezone") as f:
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
    embed: Embed = Embed(
        title="🏓 Network details",
        description=(
            f"- 🌍 Server Geo: {data['country']}, {data['region']}\n"
            f"- ⏳ Latency: {round(bot.heartbeat_latency * 1000)}ms "
        ),
        color=Color.from_rgb(90, 0, 240),
    )
    embed.set_footer(
        text=f"Matter  •  Called by @{ctx.author.username}  •  {datetime.now().strftime('%H:%M:%S')}",
        icon=ctx.author.avatar_url,
    )
    await ctx.respond(embed=embed)
