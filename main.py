from asyncio import set_event_loop_policy
from os import name

from hikari import StartedEvent

from commands.ping import ping
from instances.bot import bot, client
from instances.log import logger
from passive.presence import presence

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

logger.trace("Setting presence")
bot.listen(StartedEvent)(presence)

logger.trace("Starting bot")
bot.run()
logger.success("Matter has stopped!")
