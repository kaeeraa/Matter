"""This module contains the bot and client initialization logic."""

from os import environ

from arc import GatewayClient
from dotenv import load_dotenv
from hikari import GatewayBot, Intents

from instances.log import logger

load_dotenv()

logger.trace("Initializing bot")
bot = GatewayBot(token=environ["BOT_TOKEN"], intents=Intents.ALL)

logger.trace("Initializing client")
client = GatewayClient(app=bot)
