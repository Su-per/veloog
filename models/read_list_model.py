from sqlalchemy import Column, Integer
from ..database import Base

class ReadList(Base):
    __tablename__ = 'reply'
    user_id = Column(Integer, primary_key=True)
    post_id = Column(Integer)
