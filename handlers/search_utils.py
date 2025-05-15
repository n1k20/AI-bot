import re

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def search_google(interest):
    headers = {"User-Agent": UserAgent().random}
    query = f"топ Telegram каналов по теме {interest}"
    url = f"https://www.google.com/search?q={query}+site:tgstat.ru+OR+site:telemetr.me"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a in soup.select("a"):
        href = a.get("href")
        if href and "http" in href and ("tgstat" in href or "telemetr" in href):
            clean_link = re.search(r"https://[^&]+", href)
            if clean_link:
                links.append(clean_link.group())

    return list(set(links))[:3]  # возвращаем до 3 уникальных ссылок
