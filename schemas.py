# schemas.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username:str
    mail:str


class Accessname(BaseModel):
    name:str
    password:str
    
class Show_name(BaseModel):
    name: str

    class Config:
        from_attributes = True   # Pydantic v2 fix


class Show_Not_id(BaseModel):
    username: str
    mail: str
    creator: Optional[Show_name] = None   # ✅ FIX HERE

    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    password: str


# jwt token schema
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None