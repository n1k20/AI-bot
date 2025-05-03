import asyncio

from telethon import TelegramClient

API_ID = 25113344
API_HASH = "69e2e4cf228276b6f774da84716cc57a"

CLIENT = TelegramClient('session_name', API_ID, API_HASH)
CLIENT.start()

CHANNEL_USERNAME = "https://t.me/premium"


async def get_messages(channel_username: str) -> None:
    async for message in CLIENT.iter_messages(channel_username, limit=10):
        print(message.text)


asyncio.run(get_messages(channel_username=CHANNEL_USERNAME))
