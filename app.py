import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy

from Parser import process_message
from commands_bot import private_cmd
from config import TOKEN
from handlers import dynamic_channel_list
from handlers import user_private_router
from telegram_client import client

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
ALLOWED_UPDATES = ["message", "edited_message", "callback_query"]

# Инициализация диспетчера
dispatcher = Dispatcher(fsm_strategy=FSMStrategy.CHAT)  # Упрощенная стратегия
dispatcher.include_router(user_private_router)


async def dynamic_parsing_loop():
    try:
        await client.start()
        logger.info("Парсер каналов запущен")
        while True:
            for channel in list(dynamic_channel_list):
                try:
                    async for message in client.iter_messages(channel, limit=5):
                        await process_message(message)
                except Exception as e:
                    logger.error(f"Ошибка парсинга {channel}: {e}")
            await asyncio.sleep(60)
    except asyncio.CancelledError:
        logger.info("Парсер остановлен")
    finally:
        await client.disconnect()


async def run_bot():
    """
    Основная задача для работы бота
    """
    try:
        # Проверка токена
        me = await bot.get_me()
        logger.info(f"Бот @{me.username} запущен")

        # Настройка бота
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(commands=private_cmd)

        # Запуск поллинга
        await dispatcher.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    except Exception as error:
        logger.critical(f"Ошибка бота: {error}")
    finally:
        await bot.session.close()


async def main():
    """
    Главная функция для запуска всех задач
    """
    tasks = [
        asyncio.create_task(run_bot()),
        asyncio.create_task(dynamic_parsing_loop())
    ]

    try:
        await asyncio.gather(*tasks)

    except KeyboardInterrupt:
        logger.info("Остановка бота...")
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
    finally:
        logger.info("Бот полностью остановлен")


if __name__ == '__main__':
    asyncio.run(main())
