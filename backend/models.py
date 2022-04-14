from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

from database import Base

association_table = Table("association", Base.metadata,
                    Column("user_id", ForeignKey("users.id"), primary_key=True),
                    Column("song_id", ForeignKey("songs.id"), primary_key=True)
                    )
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    last_login = Column(DateTime)
    username = Column(String(64), nullable=False, unique=True)
    # refresh_token = Column(String(150), unique=True)

    songs = relationship(
        "Song",
        secondary=association_table,
        back_populates="users"
    )
    
    def __repr__(self):
	    return '<User {}>'.format(self.username)    

class Song(Base):
    __tablename__ = "songs"
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    title = Column(String(255), nullable=False)
    predicted_genre = Column(String(255))
    
    users = relationship(
        "User",
        secondary=association_table,
        back_populates="songs"
    )
    
    def __repr__(self):
	    return '<Title {}>'.format(self.title)
 
class Statistic(Base):
    __tablename__ = "statistics"
    
    id = Column(Integer, primary_key=True)
    most_analyzed_genre = Column(String(255))
    most_analyzed_genre_count = Column(Integer)
    total_music_analyzed = Column(Integer)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref("statistics", uselist=False))