from config import license, author, status, mail
from .dynamic_channels import add_new_channels, dynamic_channel_list
from .main_logic import process_user_message
from .telegram_search import search_channels_by_keyword
from .user_private import user_private_router

__all__ = ["process_user_message", "add_new_channels", "dynamic_channel_list", "user_private_router",
           "search_channels_by_keyword"]

__version__ = "0.0.1"
__license__ = f"{license}"
__author__ = f"{author}"
__email__ = f"{mail}"
__status__ = f"{status}"
