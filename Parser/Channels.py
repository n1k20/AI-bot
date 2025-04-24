import asyncio

from telethon.sync import TelegramClient


async def forward_post(api_id, api_hash, phone, post_url, bot_chat):
    """

    :param api_id:
    :param api_hash:
    :param phone:
    :param post_url:
    :param bot_chat:
    :return:
    """
    async with TelegramClient('Parser_session', api_id, api_hash) as client:
        await client.start(phone)
        if "/c/" in post_url:
            parts = post_url.split("/")
            chat_id = int(parts[-2])
            message_id = int(parts[-1])
        else:
            username = post_url.split("/")[-2]
            chat = await client.get_entity(username)
            chat_id = chat.id
            message_id = int(post_url.split("/")[-1])
        await client.forward_messages(bot_chat, message_id, chat_id)
        print("Пост успешно переслан!")


if __name__ == "__main__":
    asyncio.run(forward_post())
