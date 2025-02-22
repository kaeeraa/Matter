"""This module contains the presence update logic."""

from asyncio import sleep

from hikari import Activity, ActivityType, StartedEvent, Status

from matter.core.classes.bot import bot
from matter.core.classes.logger import logger


async def presence(event: StartedEvent) -> None:
    """Cycle between presences every 10 seconds

    Args:
        event (StartedEvent): an bot start event
    """
    logger.trace("Setting presence")
    while bot.is_alive:
        try:
            await bot.update_presence(
                status=Status.ONLINE,
                activity=Activity(
                    type=ActivityType.WATCHING,
                    name="/help | v#0.1.1",
                    url="https://github.com/kaeeraa/Matter",
                ),
            )
            await sleep(10)
            await bot.update_presence(
                status=Status.ONLINE,
                activity=Activity(
                    type=ActivityType.PLAYING,
                    name="with stars 🌌",
                    url="https://github.com/kaeeraa/Matter",
                ),
            )
        except KeyboardInterrupt:
            break
