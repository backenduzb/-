from aiogram import Dispatcher, Bot
from config.settings import (
    BOT_PROPERTIEST,
    BOT_TOKEN,
    DEBUG,
)
from handlers import start
from handlers.commands import story
from handlers.admin import (
    auto_m
)
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
    dp.include_routers(
        start.router,
        auto_m.router,
        story.router,
    )
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, drop_pending_updates=True)
    
if __name__ == "__main__":
    asyncio.run(main())