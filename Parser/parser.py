from handlers import add_new_channels
from services import analyze_text, parse_yandex_response
# from middlewares.DataBaseConnection import save_interest
import telethon

async def process_message(message: "telethon.tl.patched.Message"):
    """Обрабатывает сообщение из канала и добавляет релевантные каналы в список"""
    if not message.text:
        return

    try:
        # 1. Анализ текста через YandexGPT
        yandex_response = analyze_text(message.text)

        # 2. Извлечение интересов и каналов
        interest, channels = parse_yandex_response(yandex_response)

        # 3. Сохранение в базу (если нужно)
        # await save_interest(interest, message.sender.username)

        # 4. Добавление каналов в мониторинг
        add_new_channels(channels)

    except Exception as e:
        print(f"Ошибка обработки сообщения: {e}")
