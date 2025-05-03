import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy
from config import TOKEN
from commands_bot import private_cmd
from handlers import user_private_router
from parser.parser import process_message, client
from yandex import dynamic_channel_list



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
