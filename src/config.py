import os

from dotenv import load_dotenv

load_dotenv()


class InitialData:
    DB_NAME = os.environ.get("DB_NAME")
    DB_PASS = os.environ.get("DB_PASS")
    DB_USER = os.environ.get("DB_USER")
    DB_PORT = os.environ.get("DB_PORT")
    DB_HOST = os.environ.get("DB_HOST")
