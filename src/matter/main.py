"""This module contains the main entry point for the bot."""

from asyncio import set_event_loop_policy
from os import name

from hikari import StartedEvent, UnauthorizedError

from matter.core.classes.bot import bot, client
from matter.core.classes.i18n import tr
from matter.core.classes.logger import logger
from matter.core.tasks.presence import presence
from matter.plugins.ping import ping
from matter.plugins.tickets.new import new


def run() -> None:
    """Run Matter"""
    if name != "nt":
        try:
            from uvloop import EventLoopPolicy

            set_event_loop_policy(policy=EventLoopPolicy())
            logger.trace(tr("Using uvloop event loop policy"))
        except ImportError:
            logger.warning(tr("Failed to import uvloop, using default event loop policy"))

    logger.success(tr("Starting Matter"))

    logger.trace(tr("Including slash commands"))
    client.include(command=ping)
    client.include(command=new)

    logger.trace(tr("Setting presence"))
    bot.listen(StartedEvent)(presence)

    logger.trace(tr("Starting bot"))
    try:
        bot.run()
    except UnauthorizedError:
        logger.error(tr("Couldn't login in Discord. Is token valid?"))


if __name__ == "__main__":
    run()
