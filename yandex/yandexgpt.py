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

    result_text = response.json()['result']['alternatives'][0]['message']['text'].strip()
    result_lines = result_text.splitlines()

    result = {
        "topic": "",
        "channel_type": "",
        "popularity": ""
    }

    result = response.json()
    return result['result']['alternatives'][0]['message']['text'].strip()
