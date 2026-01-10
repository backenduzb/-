from aiogram import Dispatcher, Bot
from config.settings import (
    BOT_PROPERTIEST,
    BOT_TOKEN,
    DEBUG,
)
from handlers import start
import asyncio

if DEBUG:
    import logging
    logging.basicConfig(
        level = logging.INFO,
    )

async def main():
    dp = Dispatcher()
    bot = Bot(
        token=BOT_TOKEN,
        default=BOT_PROPERTIEST,
    )
    dp.include_router(start.router)
    
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())