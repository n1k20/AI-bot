from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer('Hello')


@user_private_router.message(Command('menu'))
async def echo(message: types.Message) -> None:
    await message.answer("Моя первая команда, ураааа !!!")


@user_private_router.message(Command('help'))
async def help(message: types.Message) -> None:
    await message.answer('Я помогу вам ')


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message) -> None:
    await message.answer('Здесь описание нашего тг бота')


@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message) -> None:
    await message.answer('На пожертвование разработчиков и улучшение работы бота')































