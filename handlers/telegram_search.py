
from telethon.tl.functions.contacts import SearchRequest

from telegram_client import client


async def search_channels_by_keyword(keyword: str) -> list[tuple[str, str]]:
    try:
        if not client.is_connected():
            await client.start()
        result = await client(SearchRequest(q=keyword, limit=20))
        await client.disconnect()

        channels = []
        for chat in result.chats:
            if getattr(chat, "broadcast", False) and chat.username:
                channels.append((f"@{chat.username}", chat.title))
        return channels
    except Exception as error:
        print(f"[Ошибка]: {error}")
        return []
