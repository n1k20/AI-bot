import asyncio
from aiogram import types, Bot, Router
from aiogram.filters import CommandStart, Command



user_private_router = Router()


"""
Текст или что-то другое для /start проекта
проработать текст для входа в него
то есть описание назначения бота 

"""


@user_private_router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    """
    Это функция отправляет пользователю начальный текст при его входе
    :param message: класс сообщение
    :return: ответ пользователю
    """
    await message.answer('Hello')


"""
Это самая сложная часть. Надо будет продумать диалог с пользователем.
"""

"""
Если что для понимания message.answer отправляет текстовое сообщение пользователю
это может быть как в /start так и далее 
но там можно по разному и стоит хорошо изучить библиотеку
"""

"""
Здесь в команде Command передается команда /menu
и действия который бы появились у него
"""
@user_private_router.message(Command('menu'))
async def echo(message: types.Message, bot=Bot) -> None:
    await message.answer("Моя первая команда, ураааа !!!")












