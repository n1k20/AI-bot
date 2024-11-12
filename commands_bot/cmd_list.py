from aiogram.types import BotCommand

# список всех команд которые находятся в menu
private_cmd = [BotCommand(command="menu", description="Просмотреть меню"),
               BotCommand(command="about", description="Информация о боте"),
               BotCommand(command="help", description="Помощь если что-то непонятно"),
               BotCommand(command="payment", description="Поддержка разработчиков денежными средствами"),
               BotCommand(command="profile", description="Информация о вас и вашем статусе"),
               BotCommand(command="start", description="Старт бота")]

