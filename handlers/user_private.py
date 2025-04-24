from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.formatting import as_list, as_marked_section, Bold

user_private_router = Router()

"""
-------------------------------------------------------------------------
Здесь написаны все команды для меню. Их можно можно поменять доп текстом
-------------------------------------------------------------------------
"""


@user_private_router.message(CommandStart(), Command('start'))
async def cmd_start(message: types.Message) -> None:
    text = as_list(as_marked_section(Bold("🚀 Привет! Я — твой умный помощник, который сделает Telegram еще удобнее!"),

                                     "С моей помощью ты сможешь:",

                                     "1. 🎯 Определить свои интересы — выбери темы, которые тебе интересны, а я помогу избежать лишнего шума.",
                                     "2. 📨 Получать лучшие посты — я подберу самые крутые материалы и отправлю их прямо в твой чат.",
                                     "3. ⏰ Настроить частоту — выбирай, когда и сколько постов получать.",

                                     "Давай начнем? Расскажи мне о своих предпочтениях, и я всё устрою!"))
    await message.answer(text.as_html())

    """
    # ID Username
    # принять текст интересов
    # мы должны отправить запрос в яндекс клауд
    # получить ссылки на каналы потом парсить данные и сохранить в 4 столбце
    """


@user_private_router.message(Command("update"))
async def update_cmd(message: Message, state: FSMContext) -> None:
    test = as_list(as_marked_section(Bold("Хорошо. Напишите новый данные для поиска подходящих постов")))
    await message.answer(test.as_html())


    # поменять интересы в том же месте




@user_private_router.message(Command('support'))
async def support_cmd(message: Message) -> None:
    text = as_list(
        as_marked_section(Bold("Если у вас возникли проблемы то можете написать:"), " @mayflower17",
                          " @underthinfluenc"))
    await message.answer(text.as_html())
