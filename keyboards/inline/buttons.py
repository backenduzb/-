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

async def bot_button() -> InlineKeyboardMarkup:
    
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Men haqimda", url='https://t.me/python_de_bot')]])
