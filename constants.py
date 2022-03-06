from dotenv import load_dotenv
from os import getenv

load_dotenv()

DRIVER = getenv("DRIVER")
DB_NAME = getenv("DB_NAME")
LOG_LEVEL = getenv("LOG_LEVEL")
