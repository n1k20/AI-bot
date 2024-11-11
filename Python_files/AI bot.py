import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
# библиотека для защиты TOKEN
from dotenv import find_dotenv, load_dotenv


from handlers.user_private import user_private_router


# ищет файл
load_dotenv(find_dotenv())

# наш бот через которого мы будем все писать
bot = Bot(token=os.getenv('TOKEN'))

# диспетчер через который мы будем все делать
dispatcher = Dispatcher()

dispatcher.include_router(user_private_router)


ALLOWED_UPDATES = ["message, edited_message"]



# старт проекта
async def main() -> None:
    """

    :return:
    """
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot, allowed_updates=["message"])


asyncio.run(main())
