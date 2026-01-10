from config.choicer import start_sticker
from config.settings import START_STICKERS
from utils.imports import *
from keyboards.reply.buttons import connections_button

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
        msg = await message.answer("ㅤㅤ")

        await write(
            "Assalomu alaykum, qanday savollaringiz bor?",
            bot=bot,
            chat_id=message.chat.id,
            msg_id=msg.message_id,
        )

    async with ChatActionSender(
        bot=bot, chat_id=message.from_user.id, action=ChatAction.TYPING
    ):
        await asyncio.sleep(0.5)
        msg = await message.answer("ㅤㅤ")

        await write(
            "Sizga qanday yordam berishim mumkin?",
            bot=bot,
            chat_id=message.chat.id,
            msg_id=msg.message_id,
        )
        