from aiogram.filters import BaseFilter
from aiogram.types import Message
from config.settings import ADMIN_ID

class AdminSaysChiin(BaseFilter):
    async def __call__(self, message: Message):
        text = message.text.lower()
        user_id = message.from_user.id
        return ("chiin" in text or "ちいん" in text) and user_id == ADMIN_ID

class OthersSaysChiin(BaseFilter):
    async def __call__(self, message: Message):
        text = message.text.lower()
        user_id = message.from_user.id
        return ("chiin" in text or "ちいん" in text) and user_id != ADMIN_ID

class AdminSays(BaseFilter):
    def __init__(self, text=None):
        self.text = text
        
    def __eq__(self, other):
        return bool(AdminSays(text=other))

    async def __call__(self, message: Message):

        if message.from_user.id != ADMIN_ID:
            return False

        if self.text:
            return message.text == self.text
        return True

class OthersSays(BaseFilter):
    def __init__(self, text=None):
        self.text = text
    def __eq__(self, other):
        return bool(OthersSays(other))
    
    async def __call__(self, message: Message):
        if message.from_user.id == ADMIN_ID:
            return True
        
        if self.text:
            return message.text == self.text
        return True