from sqlite3 import connect
from os.path import abspath, dirname, join

from constants import DATABASE_NAME

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def ensure_created_db(db_name: str) -> None:
    connection = connect(db_name)
    connection.close()


ensure_created_db(DATABASE_NAME)
# we can easily switch to any other SQL DB later
engine = create_engine('sqlite:///'+join(dirname(dirname(abspath(__file__))), DATABASE_NAME))
Session = sessionmaker(bind=engine)

# session = Session()