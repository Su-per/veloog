from sqlalchemy import Column, Integer, String, Date
from ..database import Base
from datetime import datetime

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    writer_id = Column(Integer)
    title = Column(String(45))
    post_thumbnail_url = Column(String(255))
    description = Column(String(255))
    date = Column(Date, default=datetime.now())
    likes = Column(Integer, default=0)
    content = Column(String(65535))
    tag = Column(String(255))