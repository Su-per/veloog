from db.base import Base
from sqlalchemy import Column, Integer


class Readlist(Base):
    __tablename__ = "readlist"

    user_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, primary_key=True)
