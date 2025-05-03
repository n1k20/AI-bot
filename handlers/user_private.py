import asyncio
import html
import re
import traceback
from typing import List

from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from parser import get_posts_for_channels
from yandex import process_user_message

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


@user_private_router.message(Command('support'))
async def support_cmd(message: Message) -> None:
    text = as_list(
        as_marked_section(Bold("Если у вас возникли проблемы то можете написать:"), " @mayflower17",
                          " @underthinfluenc"))
    await message.answer(text.as_html())


user_interests = {}
scheduler = AsyncIOScheduler(event_loop=asyncio.get_event_loop())
last_post_ids = {}

user_private_router = Router()

FREQUENCIES = {
    "immediate": 60,
    "3_hours": 10800,
    "6_hours": 21600,
    "24_hours": 86400,
    "3_days": 259200,
    "5_days": 432000
}


def get_frequency_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="По мере выхода", callback_data="freq_immediate"),
                InlineKeyboardButton(text="Пост/3 часа", callback_data="freq_3_hours"),
                InlineKeyboardButton(text="Пост/6 часов", callback_data="freq_6_hours")
            ],
            [
                InlineKeyboardButton(text="Пост/24 часа", callback_data="freq_24_hours"),
                InlineKeyboardButton(text="Пост/3 дня", callback_data="freq_3_days"),
                InlineKeyboardButton(text="Пост/5 дней", callback_data="freq_5_days")
            ]
        ]
    )


async def send_post_to_user(user_id: int, post: dict, bot):
    try:
        text = f"📢 Пост из {post['channel']}:\n\n{html.escape(post['text'])}"
        if post["links"]:
            text += "\n\n🔗 Ссылки:\n" + "\n".join(post["links"])

        print(f"[Отправка поста пользователю {user_id}] Текст: {text[:100]}...")

        if post["media"]:
            media = post["media"][0]
            if media["type"] == "photo":
                await bot.send_photo(user_id, media["id"], caption=text, parse_mode="HTML")
            elif "video" in media["type"]:
                await bot.send_video(user_id, media["id"], caption=text, parse_mode="HTML")
            elif "document" in media["type"]:
                await bot.send_document(user_id, media["id"], caption=text, parse_mode="HTML")
            else:
                await bot.send_message(user_id, text, parse_mode="HTML")
        else:
            await bot.send_message(user_id, text, parse_mode="HTML")
    except Exception as e:
        print(f"[Ошибка при отправке поста пользователю {user_id}]: {e}")
        print(f"[Traceback]: {traceback.format_exc()}")


async def schedule_posts(user_id: int, channels: List[str], frequency: int, bot):
    async def job():
        posts = await get_posts_for_channels(channels, limit=1)
        for post in posts:
            post_key = f"{post['channel']}_{post.get('id', hash(post['text']))}"
            if frequency == FREQUENCIES["immediate"]:
                if post_key not in last_post_ids.get(user_id, {}):
                    await send_post_to_user(user_id, post, bot)
                    last_post_ids.setdefault(user_id, {})[post_key] = True
            else:
                await send_post_to_user(user_id, post, bot)

    scheduler.add_job(
        job,
        trigger=IntervalTrigger(seconds=frequency),
        id=f"post_job_{user_id}",
        replace_existing=True
    )


async def send_initial_posts(user_id: int, channels: List[str], bot):
    try:
        posts = await get_posts_for_channels(channels, limit=2)
        for post in posts:
            await send_post_to_user(user_id, post, bot)
    except Exception as e:
        print(f"[Ошибка при отправке начальных постов пользователю {user_id}]: {e}")


@user_private_router.message()
async def handle_message(message: types.Message, bot):
    user_id = message.from_user.id

    if user_id in user_interests:
        interest = user_interests[user_id]["interest"]
        await message.answer(
            f"✅ Ты уже указал интерес: <b>{html.escape(interest)}</b>\n\n"
            f"🔽 Вот твои каналы ниже 👇",
            reply_markup=get_change_interest_kb(),
            parse_mode="HTML"
        )
        await message.answer(user_interests[user_id]["channels"], disable_web_page_preview=True, parse_mode="HTML")
        return

    await message.answer("🤖 Определяю твой интерес и подбираю каналы...", parse_mode="HTML")

    try:
        interest, channels_text = await process_user_message(message.text)
    except Exception as e:
        await message.answer("❌ Произошла ошибка при обработке запроса.", parse_mode="HTML")
        print(f"[Ошибка]: {e}")
        return

    user_interests[user_id] = {
        "interest": interest,
        "channels": channels_text,
        "channel_usernames": [re.sub(r"^\d+\.\s*", "", line.split(" — ")[0]) for line in channels_text.split("\n") if
                              line]  # Исправлено
    }

    try:
        text = (
            f"🧠 Я определил твой интерес: <b>{html.escape(interest)}</b>\n\n"
            f"📢 Вот топ-каналы:\n\n{html.escape(channels_text)}\n\n"
            f"⏰ Выбери, как часто получать посты:"
        )
        await message.answer(
            text,
            reply_markup=get_frequency_keyboard(),
            parse_mode="HTML"
        )
    except Exception as e:
        print(f"[Ошибка при отправке]: {e}")
        await message.answer("❌ Не удалось отправить сообщение. Возможно, ошибка форматирования.", parse_mode="HTML")


@user_private_router.callback_query(lambda c: c.data.startswith("freq_"))
async def set_frequency(callback: types.CallbackQuery, bot):
    user_id = callback.from_user.id
    freq_key = callback.data.replace("freq_", "")
    frequency = FREQUENCIES.get(freq_key)

    if not frequency:
        await callback.message.answer("❌ Неверная частота.", parse_mode="HTML")
        await callback.answer()
        return

    if user_id not in user_interests:
        await callback.message.answer("❌ Сначала выбери интерес.", parse_mode="HTML")
        await callback.answer()
        return

    user_interests[user_id]["frequency"] = frequency
    channels = user_interests[user_id]["channel_usernames"]

    # Немедленный ответ на callback
    await callback.answer()

    # Отправляем сообщение и запускаем начальные посты в фоновой задаче
    await callback.message.answer(
        f"✅ Частота установлена: {freq_key.replace('_', ' ')}.\n"
        f"Я начну присылать посты из твоих каналов!",
        parse_mode="HTML"
    )

    # Запускаем начальные посты и планировщик асинхронно
    asyncio.create_task(send_initial_posts(user_id, channels, bot))
    await schedule_posts(user_id, channels, frequency, bot)


@user_private_router.callback_query(lambda c: c.data == "change_interest")
async def change_interest_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    scheduler.remove_job(f"post_job_{user_id}", jobstore=None)
    user_interests.pop(user_id, None)
    last_post_ids.pop(user_id, None)
    await callback.message.answer("✏️ Напиши новый интерес.", parse_mode="HTML")
    await callback.answer()


def get_change_interest_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Изменить интерес", callback_data="change_interest")]
        ]
    )


scheduler.start()
