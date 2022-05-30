from tkinter.tix import Tree
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import settings

engine = create_engine(settings.SQLALCHEMY_DB_URL, echo=True)
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()
