import os
from os.path import abspath, dirname, join
from dotenv import load_dotenv


load_dotenv()

MAX_SALARY = 10000

DATABASE_NAME: str = os.getenv('DATABASE_NAME') or 'csa.db'

SERVER_PORT: int = int(os.getenv('SERVER_PORT'))
SERVER_WORKERS: int = int(os.getenv('SERVER_WORKERS'))

LOGS_DIR = join(dirname(abspath(__file__)), 'logs')
BREED_VALIDATION_ENDPOINT = "https://api.thecatapi.com/v1/breeds"
