from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboard import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(or_f(CommandStart(), Command('start'), F.text.contains("💼 Начало работы с ботом")))
async def cmd_start(message: types.Message) -> None:
    text = as_list(as_marked_section(Bold("Здравствуйте! 💐"),
                                     "Рад вас видеть, я - Бот, который поможет тебе сэкономить "
                                     "времяпрепровождение в Telegram. Нажми /about или 🤖 О боте, чтобы узнать больше"))
    await message.answer(text.as_html(), reply_markup=reply.start_keyboard)


@user_private_router.message(or_f(Command('menu'), F.text.contains("📁 Меню")))
async def menu(message: types.Message) -> None:
    text = as_list(
        as_marked_section(
            Bold("Menu bot", parse_mode=ParseMode.HTML),
            "Я могу многое 🤖 "
            "Но моя главная особенность это иметь возможность иметь данные по тематике которая тебя интересует 🛄 "
            "Это моя ключевая идея ✅"
        ),
        as_marked_section(
            Bold("Что я не могу делать: ", parse_mode=ParseMode.HTML),
            "Пока нет искуственного интеллекта",
            "Не могу полноценно разговаривать",
            "Не могу отправлять данные на другие социальные сети кроме Telegram", marker="❌"
        ),
        sep='\n                                                             \n')
    await message.answer(text.as_html(), reply_markup=reply.start_keyboard)


@user_private_router.message(or_f(Command('help'), F.text.contains("🆘 Помощь")))
async def help_cmd(message: types.Message) -> None:
    text = as_list(as_marked_section(Bold("Команды:", parse_mode=ParseMode.HTML),
                                     "🔧 /menu- Здесь находятся основные кнопки с командами, тут же вы и задаете свои приоритеты и свое дальнейшее взаимодействие с ботом",
                                     "📑 /about- Здесь содержится информация об ключевой задаче бота",
                                     "💳 /payment-  Пожертвование разработчикам для дальнейшего улучшения качества и функционала бота",
                                     "🩹 /support - Поддержка"),
                   sep="                                                                ")
    await message.answer(f'{text.as_html()}', reply_markup=reply.del_keyboard)


@user_private_router.message(or_f(Command('about'), F.text.contains("🤖О боте")))
async def about_cmd(message: types.Message) -> None:
    text = as_list(as_marked_section(
        Bold("Что делает бот 🤖 ", parse_mode=ParseMode.HTML),
        "Основной задачей бота является структурировать информацию из ваших сообществ, сделать ",
        "ее менее навязчивой, присылая только отборный контент из ваших телеграм каналов при помощи ",
        "слов-ключей, которые вы самолично задаете."),
        as_marked_section(Bold("Разработчики 👨‍💻", parse_mode=ParseMode.HTML),
                          "Nikolai Borgoyakov @may_flower17",
                          "Костров Владислав @underthinfluenc"),
        sep='                                                              '
    )
    await message.answer(f"{text.as_html()}", reply_markup=reply.del_keyboard)


@user_private_router.message(or_f(Command('payment'), F.text.contains("💸 Поддержка")))
async def payment_cmd(message: types.Message) -> None:
    text = as_marked_section(Bold("Варианты оплаты"),
                             "💳 картой в боте",
                             "💵 Переводом на Сбер",
                             marker='✅')
    await message.answer(text.as_html(), reply_markup=reply.del_keyboard)


@user_private_router.message(or_f(Command('support'), F.text.contains("📋 Поддержка")))
async def support_cmd(message: types.Message) -> None:
    text = 'Если возникли вопросы по поводу бота, нашли недочеты или баги, напишите одному из разработчиков: @underthinfluenc'
    await message.answer(f"{text}", reply_markup=reply.del_keyboard)
