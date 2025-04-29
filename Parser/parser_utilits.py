import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

def extract_telegram_channels_from_url(url):
    headers = {"User-Agent": UserAgent().random}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text()
    matches = re.findall(r"@[\w\d_]{4,}", text)
    return list(set(matches))

def is_probable_channel(username: str) -> bool:
    """
    Фильтрует каналы по шаблонам: не @admin, не @support и т.д.
    """
    bad_words = ['support', 'admin', 'help', 'bot', 'newsru', 'you']
    username_clean = username.strip('@').lower()
    return not any(bad in username_clean for bad in bad_words)