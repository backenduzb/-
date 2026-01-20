import os
import json
import aiohttp
import asyncio
import tempfile
from aiogram import types
from config.settings import BS_ID

_story_lock = asyncio.Lock()

ALLOWED_PERIODS = {21600, 43200, 86400, 172800}

async def post_story(message: types.Message, caption: str, life_time: int, video_file_id: str):
    if not BS_ID:
        return False
    if life_time not in ALLOWED_PERIODS:
        life_time = 86400
    if not video_file_id:
        return False

    async with _story_lock:
        tmp_path = None
        try:
            tg_file = await message.bot.get_file(video_file_id)

            with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
                tmp_path = f.name

            await message.bot.download_file(tg_file.file_path, destination=tmp_path)

            attach_name = "story_video"
            content = {"type": "video", "video": f"attach://{attach_name}"}

            url = f"https://api.telegram.org/bot{message.bot.token}/postStory"

            timeout = aiohttp.ClientTimeout(total=90, connect=15, sock_read=60)
            connector = aiohttp.TCPConnector(force_close=True)

            for attempt in range(2):
                try:
                    form = aiohttp.FormData()
                    form.add_field("business_connection_id", BS_ID)
                    form.add_field("content", json.dumps(content))
                    form.add_field("active_period", str(life_time))
                    form.add_field("caption", caption or "")

                    with open(tmp_path, "rb") as vf:
                        form.add_field(
                            attach_name,
                            vf,
                            filename="video.mp4",
                            content_type="video/mp4"
                        )

                        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
                            async with session.post(url, data=form) as resp:
                                text = await resp.text()
                                try:
                                    data = json.loads(text)
                                except Exception:
                                    return False

                    return bool(data.get("ok"))

                except asyncio.TimeoutError:
                    if attempt == 0:
                        await asyncio.sleep(3)  
                        continue
                    return False

        finally:
            if tmp_path and os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
