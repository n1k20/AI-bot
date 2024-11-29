from aiogram.types import BotCommand

# список всех команд которые находятся в menu
private_cmd = [BotCommand(command="menu", description="📧 Информация меню"),
               BotCommand(command="about", description="📊 Информация о боте"),
               BotCommand(command="help", description="🆘 Помощь"),
               BotCommand(command="support", description="📋 Поддержка"),
               BotCommand(command="payment", description="💳 Разработчикам"),
               BotCommand(command="start", description="💼 Начало работы с ботом"), ]
