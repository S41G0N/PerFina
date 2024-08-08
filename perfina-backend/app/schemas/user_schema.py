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

class InvoiceData(BaseModel):
    company_name: str
    company_address: str
    company_postal_code: str
    company_phone: str
    company_email: str
    company_ico: str
    company_dic: str
    company_bank_account: str
    category: str
    services: str
    rate: float
    hours: float
    invoice_number: int
    variable_symbol: str
    invoice_date: str
    invoice_due: str
    client_name: str
    client_address: str
    client_postal_code: str
    client_ico: str
    client_dic: str
