import asyncio

from telethon import TelegramClient
from config import API_ID, API_HASH

CLIENT = TelegramClient('session_name', API_ID, API_HASH)
CLIENT.start()
async def get_messages(channel_username: str, api_hash: str, api_id: int) -> None:
    async for message in CLIENT.iter_messages(channel_username, limit=10):
        print(message.text)

