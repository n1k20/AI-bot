import asyncio

from telethon.sync import TelegramClient


async def get_messages(api_id, api_hash, channel_username):
    # Получение последних 100 сообщений из канала
    async with TelegramClient('session_name', api_id, api_hash) as client:
        async for message in client.iter_messages(channel_username, limit=100):
            print("+-----------------------------------------------------+")
            # ID поста - только число
            print(message.id)
            # Это для текста
            print(message.text)
            print("+-----------------------------------------------------+")


if __name__ == "__main__":
    asyncio.run(get_messages())
