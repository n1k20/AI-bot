from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboard import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))

"""
---------------------------------------------------------------
Здесь написаны все команды для меню. Их можно можно поменять доп текстом
---------------------------------------------------------------
"""
@user_private_router.message(or_f(CommandStart(), Command('start'), F.text.contains("💼 Начало работы с ботом")))
async def cmd_start(message: types.Message) -> None:
    text = as_list(as_marked_section(Bold("🚀 Привет! Я — твой умный помощник, который сделает Telegram еще удобнее!"),

                                     "С моей помощью ты сможешь:",

                                     "1. 🎯 Определить свои интересы — выбери темы, которые тебе интересны, а я помогу избежать лишнего шума.",
                                     "2. 📨 Получать лучшие посты — я подберу самые крутые материалы и отправлю их прямо в твой чат.",
                                     "3. ⏰ Настроить частоту — выбирай, когда и сколько постов получать.",

                                     "Давай начнем? Расскажи мне о своих предпочтениях, и я всё устрою!"))
    await message.answer(text.as_html(), reply_markup=reply.start_keyboard)


@user_private_router.message(or_f(Command('support'), F.text.contains("📋 Поддержка")))
async def support_cmd(message: types.Message) -> None:
    text = as_list(
        as_marked_section(Bold("Если у вас возникли проблемы то можете написать:"), " @mayflower17",
                          " @underthinfluenc"))
    await message.answer(text.as_html(), reply_markup=reply.del_keyboard)
