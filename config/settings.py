from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True

ADMIN_ID = 6400925437

START_STICKERS = [
    "CAACAgIAAxkBAAEaBkZpYmoi-R1fcdKRa-6MBWHre3S9hgAC6TMAAgNG8UgXOI-Eu8pCCjgE",
    "CAACAgIAAxkBAAEaBi5pYme3GlT1Y_5zmNHQ7LnRkuENPwACID8AAiS88Uiw82Q9UOEMIDgE",
    "CAACAgIAAxkBAAEaBk5pYmps-k6lxglVuH8iSrVJaIVcWQACqDMAAhcg8UgOt91kvJO4PDgE",
]

BOT_TOKEN = os.getenv("BOT_TOKEN") or ""

BOT_PROPERTIEST = DefaultBotProperties(
    parse_mode="html"
)