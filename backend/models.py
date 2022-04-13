from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    username = Column(String(64), nullable=False, unique=True)
    refresh_token = Column(String(150), unique=True)

    def __repr__(self):
	    return '<User {}>'.format(self.username)    