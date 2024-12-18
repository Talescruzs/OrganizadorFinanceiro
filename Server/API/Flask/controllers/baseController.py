from dotenv import load_dotenv
from pathlib import Path
import os


class BaseController(object):
    def __init__(self):
        try:
            dotenv_path = Path('./.env')
            load_dotenv(dotenv_path=dotenv_path)
        except:
            pass
        self.host_name = os.getenv('MYSQL_HOSNAME')
        self.user_name = os.getenv('MYSQL_USER')
        self.user_password = os.getenv('MYSQL_PASSWORD')
        self.db_name = os.getenv('MYSQL_DATABASE')

