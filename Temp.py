from aiogram import Bot

async def check_webhook():
    bot = Bot(token="7876780330:AAGeFkjCfdOo0YdNZliHPWkw66eTHRsETyE")  # Замените YOUR_BOT_TOKEN на ваш токен
    webhook_info = await bot.get_webhook_info()
    print(webhook_info)
    if webhook_info.url:
        await bot.delete_webhook()
        print("Webhook удалён")
    await bot.session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(check_webhook())