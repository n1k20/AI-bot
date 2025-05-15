import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy
from telethon import TelegramClient

from Parser.parser import process_message
from commands_bot import private_cmd
from config import TOKEN, API_HASH, API_ID
from handlers import dynamic_channel_list
from handlers import user_private_router

# наш бот через которого мы будем все писать
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


client = TelegramClient("session", api_hash=API_HASH, api_id=API_ID)


async def dynamic_parsing_loop():
    await client.start()
    print("Парсер запущен. Мониторинг каналов...")
    while True:
        for channel in list(dynamic_channel_list):
            try:
                async for message in client.iter_messages(channel, limit=5):
                    await process_message(message)
            except Exception as e:
                print(f"Ошибка при парсинге {channel}: {e}")
        await asyncio.sleep(60)  # пауза между циклами


if __name__ == '__main__':
    asyncio.run(dynamic_parsing_loop())
    asyncio.run(main())
