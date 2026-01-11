from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def connections_button() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(callback_data="", text="Anonim gaplashishmoqchiman"),
            InlineKeyboardButton(url="https://uzbekdev.vercel.app", text="Developer profile"),
        ]
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=buttons,
    )
