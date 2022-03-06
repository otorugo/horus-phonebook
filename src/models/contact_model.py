from sqlalchemy import Boolean, Column, Integer, String
from connectors.sqlite_connector import db_connector


class ContactModel(db_connector.Base):
    __tablename__ = "Contact"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)
