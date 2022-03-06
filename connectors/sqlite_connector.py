from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from constants import DB_NAME, DRIVER


class SQLiteConnector:
    def __init__(self):
        self.engine = create_engine(f"{DRIVER}:///{DB_NAME}")
        self.Base = declarative_base()
        self.Session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )


db_connector = SQLiteConnector()
