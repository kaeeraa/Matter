"""
A simple ping command that returns the bot's heartbeat latency.

Example:
    /ping
"""

from arc import GatewayContext, slash_command
from hikari import Color, Embed

from instances.bot import bot
from instances.log import logger

logger.trace("Initialising ping command")


@slash_command(name="ping", description="Returns the bot's heartbeat latency.")
async def ping(ctx: GatewayContext) -> None:
    logger.trace(f"/ping command called ({ctx.author.username})")
    embed: Embed = Embed(
        title="🏓 Pong!",
        description=f"📶 Latency: {round(bot.heartbeat_latency * 1000)}ms",
        color=Color.from_rgb(200, 90, 70),
    )
    await ctx.respond(embed=embed)
