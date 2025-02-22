"""This module contains the bot and client initialization logic."""

from arc import GatewayClient
from hikari import GatewayBot, Intents

from matter.core.classes.config import Config
from matter.core.classes.logger import logger

logger.trace("Initializing bot")
bot = GatewayBot(token=Config().getToken(), intents=Intents.ALL)

logger.trace("Initializing client")
client = GatewayClient(app=bot)
