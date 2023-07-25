from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    id: int


class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
