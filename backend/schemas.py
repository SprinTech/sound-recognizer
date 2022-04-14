from pydantic import BaseModel
from datetime import datetime

class UserIn(BaseModel):
    username: str
    
    class Config:
        orm_mode=True
        
class UserCreate(UserIn):
    pass
    # refresh_token: str
    
class UserOut(UserIn):
    id: int
    created_at: datetime = None
    updated_at: datetime = None
    last_login: datetime = None
    