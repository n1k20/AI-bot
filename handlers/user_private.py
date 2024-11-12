from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f

from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message((F.text.lower().contains("привет")) | (F.text.lower().contains("здравствуйте")))
@user_private_router.message(Command('start'))
@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привет ! Я умный бот. Я помогу тебе не тратить кучу времени на поиск'
                         ' ненужной тебе информации')


@user_private_router.message(or_f(Command('menu'), F.text.lower().contains("меню")))
async def echo(message: types.Message) -> None:
    await message.answer("")


@user_private_router.message(or_f(Command('help'), F.text.lower().contains("помощь")))
async def help(message: types.Message) -> None:
    await message.answer('Я помогу вам ')


@user_private_router.message(or_f(Command('about'), F.text.lower().contains("о боте")))
async def about_cmd(message: types.Message) -> None:
    await message.answer(f"Разработчики: Nikolai Borgoyakov (TG - @mayflower17 или n1k17) - разработчик бота")
    await message.answer(f"Владислав Костров - аналитик")


@user_private_router.message((F.text.lower().contains("доставк")) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message) -> None:
    await message.answer('Можете перевести средства разработчикам в команде /about')


@user_private_router.message(Command('profile'))
async def profile_cmd(message: types.Message) -> None:
    await message.answer("Profile")
    await message.answer(f"{message.from_user.first_name}")
    await message.answer(f"{message.from_user.last_name}")
    await message.answer(f"@{message.from_user.username}")
    await message.answer(f"{message.from_user.id}")
