import os
import json
import asyncio
import tempfile
import requests
from aiogram import types
from config.settings import BS_ID

_story_lock = asyncio.Lock()
ALLOWED_PERIODS = {21600, 43200, 86400, 172800}

def _post_story_requests(url: str, data: dict, file_path: str, attach_name: str):
    headers = {
        "Expect": "",            
        "Connection": "close",   
    }
    timeout = (20, 90) 

    with open(file_path, "rb") as vf:
        files = {attach_name: ("video.mp4", vf, "video/mp4")}
        r = requests.post(url, data=data, files=files, headers=headers, timeout=timeout)
        try:
            return r.status_code, r.json()
        except Exception:
            return r.status_code, None

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
            tg_file = await asyncio.wait_for(message.bot.get_file(video_file_id), timeout=25)

            with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
                tmp_path = f.name

            await asyncio.wait_for(
                message.bot.download_file(tg_file.file_path, destination=tmp_path),
                timeout=180
            )

            attach_name = "story_video"
            content = {"type": "video", "video": f"attach://{attach_name}"}
            url = f"https://api.telegram.org/bot{message.bot.token}/postStory"

            payload = {
                "business_connection_id": BS_ID,
                "content": json.dumps(content),
                "active_period": str(life_time),
                "caption": caption or "",
            }

            for attempt in range(2):
                try:
                    status, data = await asyncio.to_thread(
                        _post_story_requests, url, payload, tmp_path, attach_name
                    )
                    if isinstance(data, dict):
                        return bool(data.get("ok"))
                except requests.RequestException:
                    pass

                if attempt == 0:
                    await asyncio.sleep(2)
                    continue

            return False

        finally:
            if tmp_path and os.path.exists(tmp_path):
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
