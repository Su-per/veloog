from tokenize import String
from db.base import Base
from sqlalchemy import Column, String


class Auth(Base):
    __tablename__ = "auth"

    email = Column(String, primary_key=True)
    code = Column(String)
