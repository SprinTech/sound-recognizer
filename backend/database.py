from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

# Define SQL Tables
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    username = db.Column(db.String(64), index=True, unique=True)
    refresh_token = db.Column(db.String(150), unique=True)

    def __repr__(self):
	    return '<User {}>'.format(self.username)    