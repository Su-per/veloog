from db.db import Base
from sqlalchemy import Column, Integer, Text, Boolean


class Reply(Base):
    __tablename__ = "replys"

    reply_id = Column(Integer, primary_key=True)
    target_id = Column(Integer)
    writer_id = Column(Integer)
    content = Column(Text)
    depth = Column(Boolean)
