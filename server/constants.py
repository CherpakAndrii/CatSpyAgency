import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_NAME: str = os.getenv('DATABASE_NAME') or 'csa.db'

SERVER_PORT: int = int(os.getenv('SERVER_PORT'))
SERVER_WORKERS: int = int(os.getenv('SERVER_WORKERS'))
