import asyncio

from telethon.sync import TelegramClient

# необходимые данные для telethon
api_id = 25113344
api_hash = "69e2e4cf228276b6f774da84716cc57a"

channel_username = f"https://t.me/premium/1"


async def get_messages(channel_username):
    """
    # post_link = f"https://t.me/premium/{message.id}"
    # текст медиа и все такое можно получить без проблем
    :param channel_username: ссылка на канал
    :return: данные текста с канала
    """
    # Получение последних 100 сообщений из канала
    async with TelegramClient('session_name', api_id, api_hash) as client:
        async for message in client.iter_messages(channel_username, limit=100):
            print("+-----------------------------------------------------+")
            # ID поста - только число
            print(message.id)
            # текст

            print("+-----------------------------------------------------+")


asyncio.run(get_messages(channel_username))
