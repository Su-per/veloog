from email.policy import default
from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(45))
    user_thumbnail_url = Column(String(255))
    veloog_id = Column(String(45), unique=True)
    show_email = Column(String(45), default='')
    show_github = Column(String(45), default='')
    show_twitter = Column(String(45), default='')
    show_facebook = Column(String(45), default='')
    show_homepage = Column(String(45), default='')
    email = Column(String(45), unique=True)
    email_recieve = Column(Boolean, default=False)