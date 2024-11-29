from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📁 Меню"),
            KeyboardButton(text="🤖 О боте"),
        ],
        [
            KeyboardButton(text="🆘 Помощь"),
            KeyboardButton(text="📋 Поддержка")
        ]
        , [
            KeyboardButton(text="💸 Поддержка разработчиков"),
            KeyboardButton(text="💼 Начало работы с ботом")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите вариант команды"
)

del_keyboard = ReplyKeyboardRemove()



"-----------------------------------------------------"



start_keyboard_2 = ReplyKeyboardBuilder()

start_keyboard_2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="О нас"),
    KeyboardButton(text="Помощь"),
    KeyboardButton(text="/payment")
)
start_keyboard_2.adjust(2, 2)

start_keyboard_3 = ReplyKeyboardBuilder()
start_keyboard_3.attach(start_keyboard_2)
start_keyboard_3.row(KeyboardButton(text="Отзыв о проекте"))

start_keyboard_4 = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Сделать опрос ", request_pull=KeyboardButtonPollType()),
    ],
        [
            KeyboardButton(text="Отправить номер ", request_contact=True),
            KeyboardButton(text="Отправить местоположение", request_location=True)
        ]
    ],
    resize_keyboard=True,
)
