from config.choicer import start_sticker
from config.settings import START_STICKERS
from filters.message import AdminSaysChiin
from utils.imports import *

router = Router()

@router.message(Command("start"))
async def start(message: types.Message, bot: Bot):
    await message.react([types.ReactionTypeEmoji(emoji="👏")])
    
    async with ChatActionSender(
        bot=bot, chat_id=message.from_user.id, action=ChatAction.CHOOSE_STICKER
    ):
        await asyncio.sleep(1)
        await message.answer_sticker(await start_sticker())

    async with ChatActionSender(
        bot=bot, chat_id=message.from_user.id, action=ChatAction.TYPING
    ):
        await asyncio.sleep(1)

        await write(
            "Assalomu alaykum, qanday savollaringiz bor?",
            message
        )

    async with ChatActionSender(
        bot=bot, chat_id=message.from_user.id, action=ChatAction.TYPING
    ):
        await asyncio.sleep(0.5)

        await write(
            "Sizga qanday yordam berishim mumkin?",
            message
        )
        
@router.business_message(AdminSaysChiin())
async def bussines_start(message: types.Message, bot: Bot):
    await message.answer_sticker(await start_sticker())
    msg = await write(
        "こんいちわ, Javohir qanaqasiz!",
        message=message
    )