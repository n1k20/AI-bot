from telethon import TelegramClient
from telethon.tl.functions.contacts import SearchRequest

from config import API_ID, API_HASH

client = TelegramClient("search_session", API_ID, API_HASH)


async def search_channels_by_keyword(keyword: str) -> list[tuple[str, str]]:
    await client.start()
    result = await client(SearchRequest(q=keyword, limit=20))
    await client.disconnect()

    channels = []
    for chat in result.chats:
        if getattr(chat, "broadcast", False) and chat.username:
            channels.append((f"@{chat.username}", chat.title))
    return channels
