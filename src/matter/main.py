"""This module contains the main entry point for the bot."""

from asyncio import set_event_loop_policy
from os import name

from hikari import StartedEvent

from matter.plugins.ping import ping
from matter.plugins.newTicket import newTicket
from matter.core.classes.bot import bot, client
from matter.core.classes.logger import logger
from matter.core.tasks.presence import presence


def run() -> None:
    if name != "nt":
        try:
            from uvloop import EventLoopPolicy

            set_event_loop_policy(policy=EventLoopPolicy())
            logger.trace("Using uvloop event loop policy")
        except ImportError:
            logger.warning("Failed to import uvloop, using default event loop policy")

    logger.success("Starting Matter")

    logger.trace("Including slash commands")
    client.include(command=ping)
    client.include(command=newTicket)

    logger.trace("Setting presence")
    bot.listen(StartedEvent)(presence)

    logger.trace("Starting bot")
    bot.run()


if __name__ == "__main__":
    run()
