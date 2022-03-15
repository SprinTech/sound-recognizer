from main import Base
from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(64), index=True, unique=True)
	refresh_token = Column(String(150), index=True, unique=True)
	playlist_id_short = Column(String(30), index=True, unique=True)
	playlist_id_medium = Column(String(30), index=True, unique=True)
	playlist_id_long = Column(String(30), index=True, unique=True)

	def __repr__(self):
		return '<User {}>'.format(self.username)    