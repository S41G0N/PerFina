from typing import Union

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from db.config import TORTOISE_ORM
from api.routes import transactions


app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.include_router(transactions.router)
