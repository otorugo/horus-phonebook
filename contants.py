from dotenv import load_dotenv
from os import getenv

load_dotenv()

CONN_STRING = getenv("CONN_STRING")
