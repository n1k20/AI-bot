from telethon import TelegramClient

from config import API_ID, API_HASH

client = TelegramClient("search_session", API_ID, API_HASH)


async def main():
    await client.start()  # ВАЖНО: ничего не передавать!
    print("✅ Авторизация прошла успешно")


with client:
    client.loop.run_until_complete(main())
