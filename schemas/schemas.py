from pydantic import BaseModel


class SchemaAddIncome(BaseModel):
    description: str
    amount: int


class SchemaRemoveIncome(BaseModel):
    description: str
    amount: int
