from telegram_client import client


async def main():
    try:
        if not client.is_connected():
            await client.start()
        print("✅ Авторизация прошла успешно")
    except Exception as error:
        print(f"Ошибка : {error}")

with client:
    client.loop.run_until_complete(main())
