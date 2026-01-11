from aiogram.filters import BaseFilter
from aiogram.types import Message
from config.settings import ADMIN_ID

class AdminSaysChiin(BaseFilter):
    async def __call__(self, message: Message):
        text = message.text.lower()
        user_id = message.from_user.id
        return "chiin" in text or "ちいん" in text and user_id == ADMIN_ID