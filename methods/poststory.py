import json
import aiohttp
import tempfile
from config.settings import BS_ID
from utils.imports import *

async def post_story(message: types.Message, caption: str, life_time: int,video_file_id:str ):
    tg_file = await message.bot.get_file(video_file_id)

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
        tmp_path = f.name

    await message.bot.download_file(tg_file.file_path, destination=tmp_path)

    attach_name = "story_video"
    content = {
        "type": "video",
        "video": f"attach://{attach_name}",
    }

    form = aiohttp.FormData()
    form.add_field("business_connection_id", BS_ID)
    form.add_field("content", json.dumps(content))
    form.add_field("active_period", "86400")
    form.add_field("caption", caption or "")

    with open(tmp_path, "rb") as vf:
        form.add_field(
            attach_name,
            vf,
            filename="video.mp4",
            content_type="video/mp4"
        )

        url = f"https://api.telegram.org/bot{message.bot.token}/postStory"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=form) as resp:
                data = await resp.json()

    if not data.get("ok"):
        print(f"Xatolik: {data}")
        return f"Xatolik: {data}"
    else:
        return True
