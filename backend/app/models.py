from sqlalchemy import Column, Integer, String

from database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer)
    username = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
