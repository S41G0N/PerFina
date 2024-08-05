#models/transaction.py
from tortoise import fields, models


class Category(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)


class Transaction(models.Model):
    id = fields.IntField(pk=True)
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    category = fields.ForeignKeyField("models.Category", related_name="transactions")
