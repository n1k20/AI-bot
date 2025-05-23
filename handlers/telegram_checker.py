
from telethon.errors import UsernameInvalidError, UsernameNotOccupiedError
from telethon.tl.functions.contacts import ResolveUsernameRequest

from telegram_client import client

async def is_channel(username: str) -> bool:
    """
    Проверяет, является ли указанный @username Telegram-каналом.
    Возвращает True, если это публичный канал (broadcast).
    """
    username = username.strip("@")
    try:
        entity = await client(ResolveUsernameRequest(username))
        if entity and entity.chats:
            chat = entity.chats[0]
            return getattr(chat, "broadcast", False)
    except (UsernameInvalidError, UsernameNotOccupiedError):
        return False
    except Exception as e:
        print(f"[❗️] Ошибка при проверке {username}: {e}")
        return False
    return False
