# schemas/transaction_schema.py
from pydantic import BaseModel


class TransactionCreate(BaseModel):
    amount: float
    category: str


class TransactionResponse(BaseModel):
    id: int
    amount: float
    category: str

    class Config:
        from_attributes = True
