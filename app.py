import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy
# библиотека для защиты TOKEN
from dotenv import find_dotenv, load_dotenv

from commands_bot.cmd_list import private_cmd
from handlers.user_private import user_private_router

# ищет файл
load_dotenv(find_dotenv())

# наш бот через которого мы будем все писать
TOKEN = '7876780330:AAGeFkjCfdOo0YdNZliHPWkw66eTHRsETyE'
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []

ALLOWED_UPDATES = ["message, edited_message"]

# диспетчер через который мы будем все делать
dispatcher = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)
dispatcher.include_router(user_private_router)


# великий main
async def main():
    # убираем ответы бота на запросы пользователей
    # чтобы бот не перегружался
    await bot.delete_webhook(drop_pending_updates=True)

    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())

    # в private_cmd список всех команд в menu для приватного бота
    await bot.set_my_commands(commands=private_cmd, scope=types.BotCommandScopeAllPrivateChats())

    await dispatcher.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


# запуск бота
if __name__ == '__main__':
    asyncio.run(main())
