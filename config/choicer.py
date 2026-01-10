from random import choice
from .settings import START_STICKERS

async def start_sticker() -> str:
    return choice(START_STICKERS)