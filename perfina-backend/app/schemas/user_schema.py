from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from models.user_model import User
UserPydantic = pydantic_model_creator(User, name="User", exclude=("hashed_password",))

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

