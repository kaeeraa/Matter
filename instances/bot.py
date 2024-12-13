"""This module contains the bot and client initialization logic."""

from arc import GatewayClient
from hikari import GatewayBot, Intents

from instances.config import Config
from instances.log import logger

logger.trace("Initializing bot")
bot = GatewayBot(token=Config().getToken(), intents=Intents.ALL)

logger.trace("Initializing client")
client = GatewayClient(app=bot)
