from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[],
    resize_keyboard=True,
    input_field_placeholder="Выберите вариант команды"
)

del_keyboard = ReplyKeyboardRemove()
