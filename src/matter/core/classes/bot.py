"""This module contains the bot and client initialization logic."""

from arc import GatewayClient
from hikari import GatewayBot, Intents

from matter.core.classes.config import Config
from matter.core.classes.i18n import tr
from matter.core.classes.logger import logger

logger.trace(tr("Initializing bot"))
_token: str = Config().getDictionary("bot").get("token", "")
bot = GatewayBot(token=_token, intents=Intents.ALL)

logger.trace(tr("Initializing client"))
client = GatewayClient(app=bot)
