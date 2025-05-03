import asyncio

from aiogram import Bot


async def check_webhook(TOKEN: str) -> None:
    bot = Bot(token=TOKEN)
    webhook_info = await bot.get_webhook_info()
    print(webhook_info)
    if webhook_info.url:
        await bot.delete_webhook()
        print("Webhook удалён")
    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(check_webhook())
