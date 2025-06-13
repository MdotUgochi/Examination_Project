from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: EmailStr
    

class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
     name: Optional[str] = None
     email: Optional[EmailStr] = None
     is_active: Optional[bool] = None


     
class User(UserBase):
     id: UUID
     is_active: bool = True

     class Config:
         from_attributes = True



