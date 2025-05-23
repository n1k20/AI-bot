from config import author, mail, status, license
from services.yandexgpt import analyze_text, parse_yandex_response

__all__ = ["analyze_text", "parse_yandex_response"]

__author__ = f"{author}"
__email__ = f"{mail}"
__license__ = f"{license}"
__status__ = f"{status}"
