from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.enums import ParseMode
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from filters.chat_types import ChatTypeFilter
from keyboard import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(or_f(CommandStart(), Command('start'),
                                  (F.text.lower().contains("привет")) | (F.text.lower().contains("здравствуйте"))))
async def cmd_start(message: types.Message) -> None:
    await message.answer(
        f'Привет {message.from_user.full_name} ! Я умный бот. Я помогу тебе не тратить кучу времени на поиск'
        ' ненужной тебе информации', reply_markup=reply.start_keyboard_2.as_markup(
            resize_keyboard=True,
            input_field_placeholder="Выберите вариант команды"
        ))


@user_private_router.message(or_f(Command('menu'), F.text.lower().contains("меню")))
async def echo(message: types.Message) -> None:
    text = as_list(
        as_marked_section(
            Bold("Menu bot"),
            "Я могу многое 🤖 "
            "Но моя главная особенность это иметь возможность иметь данные по тематике которая тебя интересует 🛄 "
            "Это моя ключевая идея"
    )),
    as_marked_section(
        Bold("Что я не могу делать"),
        "Пока нет искуственного интеллекта"
    ),
    sep='\n----------------------------------\n'
    await message.answer("<b>Presssss F:</b>", parse_mode=ParseMode.HTML, reply_markup=reply.del_keyboard)


@user_private_router.message(or_f(Command('help'), F.text.lower().contains("помощь")))
async def help(message: types.Message) -> None:
    await message.answer('Я помогу вам', reply_markup=reply.del_keyboard)


@user_private_router.message(or_f(Command('about'), F.text.lower().contains("о боте")))
async def about_cmd(message: types.Message) -> None:
    await message.answer(f"Разработчики: Nikolai Borgoyakov (TG - @mayflower17 или n1k17) - разработчик бота",
                         reply_markup=reply.del_keyboard)
    await message.answer(f"Владислав Костров - аналитик ")


@user_private_router.message((F.text.lower().contains("поддержка")) | (F.text.lower() == 'варианты оплаты'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message) -> None:
    text = as_marked_section(Bold("Варианты оплаты"),
                             "💳 картой в боте",
                             "💵 Переводом на Сбер",
                             marker='✅ ')
    await message.answer(text.as_html(), reply_markup=reply.del_keyboard)


@user_private_router.message(Command('profile'))
async def profile_cmd(message: types.Message) -> None:
    await message.answer("<b> You profile: </b>", parse_mode=ParseMode.HTML)
    await message.answer("DATA:")
    await message.answer(f"{message.from_user.first_name}")
    await message.answer(f"{message.from_user.last_name}")
    await message.answer(f"@{message.from_user.username}")
    await message.answer(f"{message.from_user.id}")



@user_private_router.message(F.contact)
async def contact_cmd(message: types.Message) -> None:
    await message.answer("Ваш номер телефона")
    await message.answer(str(message.contact.phone_number))

@user_private_router.message(F.location)
async def location_cmd(message: types.Message) -> None:
    await message.answer("Ваше местоположение")
    await message.answer(str(message.location))







