from aiogram.types import BotCommand

# список всех команд которые находятся в menu
private_cmd = [BotCommand(command="menu", description="📧 Информация меню"),
               BotCommand(command="about", description="📊 Информация о боте"),
               BotCommand(command="help", description="🆘 Помощь"),
               BotCommand(command="payment", description="💳 Поддержка разработчиков"),
               BotCommand(command="profile", description="👨‍💼 Ваш профиль"),
               BotCommand(command="start", description="⭐ Начало работы с ботом")]