import re
from typing import List, Optional

from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

from config import API_ID, API_HASH

client = TelegramClient("post_parser", API_ID, API_HASH)


async def parse_latest_post(channel_username: str, limit: int = 1) -> List[Optional[dict]]:
    try:
        if not client.is_connected():
            await client.start()

        username = channel_username.strip("@")
        posts = []
        async for message in client.iter_messages(f"@{username}", limit=limit):
            post_data = {
                "id": message.id,
                "text": message.text or "",
                "media": [],
                "links": [],
                "channel": channel_username
            }

            if message.media:
                if isinstance(message.media, MessageMediaPhoto):
                    post_data["media"].append({"type": "photo", "id": message.media.photo.id})
                elif isinstance(message.media, MessageMediaDocument):
                    doc = message.media.document
                    mime_type = getattr(doc, "mime_type", "")
                    post_data["media"].append({"type": mime_type, "id": doc.id})

            if message.text:
                urls = re.findall(r"https?://[^\s]+", message.text)
                post_data["links"].extend(urls)

            if message.reply_markup:
                for row in message.reply_markup.rows:
                    for button in row.buttons:
                        if hasattr(button, "url") and button.url:
                            post_data["links"].append(button.url)

            posts.append(post_data)

        return posts

    except Exception as e:
        print(f"[Ошибка при парсинге {channel_username}]: {e}")
        return []
    finally:
        if client.is_connected():
            await client.disconnect()


async def get_posts_for_channels(channels: List[str], limit: int = 1) -> List[dict]:
    posts = []
    for channel in channels:
        channel_posts = await parse_latest_post(channel, limit=limit)
        posts.extend(channel_posts)
    return posts
