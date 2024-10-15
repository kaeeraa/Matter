from hikari import GatewayBot
from dotenv import load_dotenv
from os import environ

load_dotenv()

bot = GatewayBot(token=environ["BOT_TOKEN"])
