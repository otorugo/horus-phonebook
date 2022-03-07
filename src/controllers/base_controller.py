# from connectors.db import mysql_connector, Base
# from pydantic import BaseModel
from typing import List
from connectors.sqlite_connector import db_connector
from utils.logger import base_logger


class BaseController:
    def __init__(self) -> None:
        self.database_connector = db_connector
        self.Session = self.database_connector.Session

    def __enter__(self):
        base_logger.info("Opening db session...")
        self.session = self.Session()
        return self.session

    def __exit__(self, *exc):
        base_logger.info("Closing db session...")
        self.session.close()
        base_logger.info("Closed db session")

    def to_dict(self, row) -> dict:
        data_dict = {}
        for column in row.__table__.columns:
            data_dict[column.name] = str(getattr(row, column.name))

        return data_dict

    def to_dict_list(self, rows: List) -> List[dict]:
        parsed_list = list(map(self.to_dict, rows))
        return parsed_list
