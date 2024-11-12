from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f

user_private_router = Router()


@user_private_router.message((F.text.lower().contains("привет")) | (F.text.lower().contains("здравствуйте")))
@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Hello')


@user_private_router.message(or_f(Command('menu'), F.text.lower().contains("меню")))
async def echo(message: types.Message) -> None:
    await message.answer("Моя первая команда, ураааа !!!")


@user_private_router.message(or_f(Command('help'), F.text.lower().contains("помощь")))
async def help(message: types.Message) -> None:
    await message.answer('Я помогу вам ')


@user_private_router.message(or_f(Command('about'), F.text.lower().contains("о боте")))
async def about_cmd(message: types.Message) -> None:
    await message.answer('Здесь описание нашего тг бота')


@user_private_router.message((F.text.lower().contains("доставк")) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message) -> None:
    await message.answer('На пожертвование разработчиков и улучшение работы бота')
