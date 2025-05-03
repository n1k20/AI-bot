from handlers.yandexgpt import analyze_text
from handlers.telegram_search import search_channels_by_keyword

async def process_user_message(user_text: str) -> tuple[str, str]:
    interest = analyze_text(user_text).lower().strip()

    # Подчищаем особые случаи
    if interest in ("it", "айти"):
        interest = "технологии"
    elif interest == "видеоигры":
        interest = "игры"

    channels = await search_channels_by_keyword(interest)

    if not channels:
        return interest, "😔 Каналы по этой теме не найдены."

    # ВОТ ЗДЕСЬ — выводим до 10 каналов
    formatted = "\n".join([
        f"{i+1}. {ch[0]} — {ch[1]}" for i, ch in enumerate(channels[:10])
    ])
    return interest, formatted
