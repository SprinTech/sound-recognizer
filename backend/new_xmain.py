from flask import Flask
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)

engine = create_engine("sqlite:///../sound_recognizer.db")

if not database_exists(engine.url):
    create_database(engine.url)
    
# create session and base declarative
Session = sessionmaker(bind=engine)

Base = declarative_base()

# make sure user table is created
Base.metadata.create_all(engine)
