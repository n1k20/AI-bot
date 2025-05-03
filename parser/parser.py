from telethon import TelegramClient
from config import API_ID, API_HASH
from yandex.yandexgpt import analyze_text, parse_yandex_response
from middlewares.DataBaseConnection import save_interest
from yandex.dynamic_channels import add_new_channels

client = TelegramClient('session_name', API_ID, API_HASH)

async def process_message(message):
    if message.text:
        yandex_response = analyze_text(message.text)
        interest, channels = parse_yandex_response(yandex_response)
        username = message.sender.username if message.sender else "unknown"
        await save_interest(interest, username)
        add_new_channels(channels)