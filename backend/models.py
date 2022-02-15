from sqlalchemy import Column, Integer, String
from database import Base

class AudioFile(Base):
    """
    Create AudioFile database
    """
    __tablename__ = "audiofile"

    id = Column(Integer, primary_key=True)
    genre = Column(String, nullable=False)
    path = Column(String, nullable=False, unique=True)