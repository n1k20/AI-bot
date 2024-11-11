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

"""
Текст или что-то другое для /start проекта
проработать текст для входа в него
то есть описание назначения бота 

"""


@dispatcher.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Hello')


"""
Это самая сложная часть. Надо будет продумать диалог с пользователем, как он будет выглядеть.
Но я думаю в плане mMVP это пока не надо 
"""

"""
Если что для понимания message.answer отправляет текстовое сообщение пользователю
это может быть как в /start так и далее 
"""


@dispatcher.message()
async def echo(message: types.Message, bot=Bot) -> None:
    await bot.send_message(message.from_user.id, 'Ответ')
    user_words = message.text.lower().split()
    answer_one = ['hello', 'привет', 'good day', 'hi', 'здравствуйте']

    if any(word in answer_one for word in user_words):
        await message.answer('Приветствую вас в моем чате. AI bot !!!!')
    elif len(user_words[0]) > 0:
        await message.answer('Но почему бота писать так сложно')
    else:
        await message.answer(message.text)


# старт проекта
async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


asyncio.run(main())
