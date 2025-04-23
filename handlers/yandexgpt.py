import requests
from handlers.config import API_KEY, FOLDER_ID, YANDEX_URL

def analyze_text(text: str) -> str:
    payload = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {"stream": False, "temperature": 0.6, "maxTokens": "200"},
        "messages": [
            {
                "role": "system",
                "text": "Ты помощник, который определяет интерес человека по тексту и предлагает каналы в Telegram по теме."
            },
            {
                "role": "user",
                "text": f"Вот сообщение: {text}\nОпредели интерес и предложи 3 Telegram-канала, которые подойдут для него. Формат: \nИнтерес: ... \nКаналы: \n1. @channel1\n2. @channel2\n3. @channel3"
            }
        ]
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Api-Key {API_KEY}"}
    response = requests.post(YANDEX_URL, headers=headers, json=payload)
    return response.json()['result']['alternatives'][0]['message']['text'].strip()

def parse_yandex_response(response_text: str):
    lines = response_text.strip().splitlines()
    interest = lines[0].replace("Интерес:", "").strip()
    channels = [line.split(".", 1)[1].strip() for line in lines[2:] if line.strip()]
    return interest, channels
