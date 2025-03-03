"""This module contains the bot and client initialization logic."""

from typing import Any

from arc import GatewayClient
from hikari import GatewayBot, Intents

from matter.core.classes.config import Config
from matter.core.classes.i18n import tr
from matter.core.classes.logger import logger

BOT_CONFIG: dict[Any, Any] = Config().getDict("bot", {})
TOKEN: str = BOT_CONFIG.get("token", "")

logger.trace(tr("Initializing bot"))

bot = GatewayBot(token=TOKEN, intents=Intents.ALL)

logger.trace(tr("Initializing client"))
client = GatewayClient(app=bot)
