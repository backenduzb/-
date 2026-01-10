import asyncio
from aiogram import Bot

async def write(text: str, bot: Bot, chat_id: int, msg_id: int):
    words = text.split()
    message_text = ""
        
    for word in words:
        message_text += word + " "
        try:
                await bot.edit_message_text(
                    text=message_text.strip(),  
                    chat_id=chat_id,
                    message_id=msg_id
                )
                await asyncio.sleep(0.2)
        except:
            pass