import re
from typing import Any

import requests

from config import API_KEY, FOLDER_ID, YANDEX_URL


def analyze_text(text: str) -> dict[str, str | Any]:
    prompt = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt",
        "completionOptions": {"stream": False, "temperature": 0.4, "maxTokens": "1000"},
        "messages": [
            {
                "role": "system",
                "text": "Ты — профессиональный классификатор интересов пользователей.\n"
                        "Твоя задача: на основе запроса пользователя выдать наиболее точную и узкую категорию интереса.\n"
                        "Отвечай одним-двумя словами (например: Python, Баскетбол, Криптовалюта, Стартапы).\n"
                        "Не обобщай (не Технологии, а Python; не Спорт, а Баскетбол).Только при условии что у него не написано Спорт, Технологии, а указано что то конкретное\n"
                        "Не добавляй описаний, не придумывай списков каналов. Только название интереса.\n"
            },
            {
                "role": "user",
                "text": text
            }
        ]
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Api-Key {API_KEY}"}
    response = requests.post(YANDEX_URL, headers=headers, json=prompt)

    # Ответ от Yandex Cloud
    result = response.json()['result']['alternatives'][0]['message']['text'].strip()

    return result


def parse_yandex_response(response_text: str) -> tuple[str, str]:
    """
    Извлекает интерес и текстовый ответ из ответа YandexGPT.
    Предполагается, что YandexGPT возвращает текст вроде:
    "Интерес: программирование\n\nОписание: Это..."
    """

    # Поиск строки "Интерес: ..."
    interest_match = re.search(r"Интерес\s*[:\-]\s*(.+)", response_text, re.IGNORECASE)
    interest = interest_match.group(1).strip().lower() if interest_match else "неопределено"

    words = list(dict.fromkeys([word.strip() for word in re.split(r"[,\n]", interest)]))  # убираем повторы
    interest = ", ".join(words)

    return interest, response_text.strip()
