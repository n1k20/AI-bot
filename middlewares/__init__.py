from config import author, mail, status, license
from .DataBaseConnection import connect_db

__all__ = ["connect_db"]
__license__ = f"{license}"
__author__ = f"{author}"
__email__ = f"{mail}"
__status__ = f"{status}"
