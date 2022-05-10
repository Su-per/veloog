from sqlalchemy import Column, Integer, String
from ..database import Base

class Reply(Base):
    __tablename__ = 'reply'
    reply_id = Column(Integer, primary_key=True, autoincrement=True)
    target_id = Column(Integer)
    writer_id = Column(Integer)
    content = Column(String(255))
    depth = Column(Integer)
