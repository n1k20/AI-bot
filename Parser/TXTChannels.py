import asyncio

from telethon.sync import TelegramClient


async def get_messages(api_id, api_hash, channel_username):
    """
    # post_link = f"https://t.me/premium/{message.id}"
    # текст медиа и все такое можно получить без проблем
    :param api_id:
    :param api_hash:
    :param channel_username:
    :return:
    """
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
