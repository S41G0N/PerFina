#api/routes/transactions.py
from fastapi import APIRouter, HTTPException
from models.transaction_model import Transaction, Category
from schemas.transaction_schema import TransactionCreate, TransactionResponse
from tortoise.contrib.pydantic import pydantic_model_creator

router = APIRouter()

Transaction_Pydantic = pydantic_model_creator(Transaction, name="Transaction")


@router.post("/transactions/", response_model=TransactionResponse)
async def create_transaction(new_transaction: TransactionCreate):

    category, _ = await Category.get_or_create(name=new_transaction.category)
    db_transaction = await Transaction.create(
        amount=new_transaction.amount,
        category=category,
    )
    return TransactionResponse(
        id=db_transaction.id,
        amount=float(db_transaction.amount),
        category=category.name,
    )


@router.get("/transactions/{transaction_id}", response_model=TransactionResponse)
async def read_transaction(transaction_id: int):
    transaction = await Transaction.get_or_none(id=transaction_id).prefetch_related(
        "category"
    )
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {
        "id": transaction.id,
        "amount": float(transaction.amount),
        "category": transaction.category.name if transaction.category else None,
    }
