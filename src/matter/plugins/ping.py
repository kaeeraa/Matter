"""
A simple ping command that returns the bot's heartbeat latency.

Example:
    /ping
"""

from json import load
from typing import Any
from urllib.error import URLError
from urllib.request import urlopen

from arc import GatewayContext, slash_command

from matter.core.classes.bot import bot
from matter.core.classes.i18n import tr
from matter.core.classes.logger import logger
from matter.core.helpers.embed import embed

COMMAND_NAME = "ping"
COMMAND_DESCRIPTION: str = tr("Returns the bot's heartbeat latency.")

data: dict[str, Any] = {}

try:
    with urlopen("http://ip-api.com/json/?fields=country,regionName,city", timeout=5) as f:
        data = load(f)
except URLError:
    logger.error(tr("Failed to get server geo data"))


@slash_command(name=COMMAND_NAME, description=COMMAND_DESCRIPTION)
async def ping(ctx: GatewayContext) -> None:
    """/ping command"""
    logger.trace(tr("/{command} command called ({author})").format(command=COMMAND_NAME, author=ctx.author.username))

    try:
        country: str = data.get("country", tr("Unknown"))
        region: str = data.get("city", tr("Unknown"))
        latency: int | str = round(bot.heartbeat_latency * 1000) if bot.heartbeat_latency else tr("Unavailable")

        description: str = tr("- 🌍 Server Geo: {country}, {region}\n- ⏳ Latency: {latency}ms").format(
            country=country, region=region, latency=latency
        )

        await ctx.respond(
            embed=embed(
                author=ctx.author,
                title=tr("🏓 Network details"),
                description=description,
            )
        )
    except (ValueError, TypeError):
        raise RuntimeWarning(tr("Could not fetch current geo")) from None
