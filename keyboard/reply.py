from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/menu"),
            KeyboardButton(text="/about"),
    ],
        [
            KeyboardButton(text="/help"),
            KeyboardButton(text="/payment")
        ]
],
    resize_keyboard=True,
    input_field_placeholder="Выберите вариант команды"

)

del_keyboard = ReplyKeyboardRemove()


start_keyboard_2 = ReplyKeyboardBuilder()

start_keyboard_2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="О нас"),
    KeyboardButton(text="Помощь"),
    KeyboardButton(text="/payment")
)
start_keyboard_2.adjust(2, 2)














