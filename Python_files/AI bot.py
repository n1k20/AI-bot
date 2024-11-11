import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
# библиотека для защиты TOKEN
from dotenv import find_dotenv, load_dotenv

# ищет файл
load_dotenv(find_dotenv())

# наш бот через которого мы будем все писать
bot = Bot(token=os.getenv('TOKEN'))

# диспетчер через который мы будем все делать
dispatcher = Dispatcher()



ALLOWED_UPDATES = ["message, edited_message"]



# старт проекта
async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot, allowed_updates=["message"])


asyncio.run(main())
