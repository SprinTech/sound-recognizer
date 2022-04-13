from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Database

SQLALCHEMY_DATABASE_URL = f"postgresql://{Database.USER}:{Database.PASSWORD}@{Database.HOST}/{Database.DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()