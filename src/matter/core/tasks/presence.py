"""This module contains the presence update logic."""

from asyncio import sleep

from hikari import Activity, ActivityType, StartedEvent, Status

from matter.build.BuildConfig import build
from matter.core.classes.bot import bot
from matter.core.classes.logger import logger


async def presence(event: StartedEvent) -> None:
    """Cycle between presences every 10 seconds

    Args:
        event (StartedEvent): an bot start event
    """
    logger.trace("Setting presence")

    version: str = build.get("version")

    while bot.is_alive:
        try:
            await bot.update_presence(
                status=Status.ONLINE,
                activity=Activity(
                    type=ActivityType.WATCHING,
                    name=f"/help | v#{version}",
                    url="https://github.com/kaeeraa/Matter",
                ),
            )
            await sleep(10)
            await bot.update_presence(
                status=Status.ONLINE,
                activity=Activity(
                    type=ActivityType.WATCHING,
                    name="stars 🌌",
                    url="https://github.com/kaeeraa/Matter",
                ),
            )
            await sleep(10)
        except KeyboardInterrupt:
            break
