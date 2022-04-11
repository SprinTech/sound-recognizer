from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    
class UserCreate(UserBase):
    refresh_token: str
    
class User(UserBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    