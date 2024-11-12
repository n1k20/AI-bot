import asyncio
import os

from aiogram import Bot, Dispatcher, types
# библиотека для защиты TOKEN
from dotenv import find_dotenv, load_dotenv

from commands_bot.cmd_list import private_cmd
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router




# ищет файл
load_dotenv(find_dotenv())

# наш бот через которого мы будем все писать
bot = Bot(token=os.getenv('TOKEN'))
ALLOWED_UPDATES = ["message, edited_message"]

# диспетчер через который мы будем все делать
dispatcher = Dispatcher()
dispatcher.include_router(user_private_router)
dispatcher.include_router(user_group_router)

# старт проекта
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private_cmd, scope=types.BotCommandScopeAllPrivateChats())
    await dispatcher.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
