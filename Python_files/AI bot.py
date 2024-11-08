import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from config import TOKEN

bot = Bot(token=TOKEN)
dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Hello')


@dispatcher.message()
async def echo(message: types.Message) -> None:
    user_words = message.text.lower().split()
    answer_one = ['hello', 'привет', 'good day', 'hi', 'здравствуйте']
    if any(word in answer_one for word in user_words):
        await message.answer('Приветствую вас в моем чате. AI bot !!!!')
    elif len(user_words[0]) > 0:
        await message.answer('Ты че не здароваешься')
    else:
        await message.answer(message.text)


async def main() -> None:
    await dispatcher.start_polling(bot)


asyncio.run(main())
