from asyncio import sleep

from hikari import Activity, ActivityType, StartedEvent, Status

from instances.bot import bot
from instances.log import logger


async def presence(event: StartedEvent) -> None:
    """
    An event listener that updates the bot's presence every 10 seconds.

    The activity changes between watching info and playing with stars.
    """
    logger.trace("Setting presence")
    while 1:
        try:
            await bot.update_presence(
                status=Status.ONLINE,
                activity=Activity(
                    type=ActivityType.WATCHING,
                    name="/help | v#0.1.0",
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
