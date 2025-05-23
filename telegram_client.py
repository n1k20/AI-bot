from telethon import TelegramClient

from config import API_ID, API_HASH

client = TelegramClient('main_session', API_ID, API_HASH, system_version="4.16.30-vxCustom")