from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def connections_button() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Anonim gaplashishmoqchiman"), KeyboardButton(text="Developer profile")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )