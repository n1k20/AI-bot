from config import author, mail, license, status
from .parser import process_message
from .post_parser import get_posts_for_channels

__all__ = ["get_posts_for_channels", "process_message"]
__version__ = "0.0.1"

__author__ = f"{author}"
__license__ = f"{license}"
__email__ = f"{mail}"
__status__ = f"{status}"
