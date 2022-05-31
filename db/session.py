from core.config import settings
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine(settings.SQLALCHEMY_DB_URL, echo=False)


def get_db():
    db = Session(bind=engine)
    return db
