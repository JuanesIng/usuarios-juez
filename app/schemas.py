from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    user = "user"
    admin = "admin"

class UserBase(BaseModel):
    first_name: str
    last_name: str
    password: str
    email: str
    role: UserRole = UserRole.user

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]
    role: Optional[UserRole]

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  

class Token(BaseModel):
    access_token: str
    token_type: str
