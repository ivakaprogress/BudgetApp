from fastapi import APIRouter
from classes.budget import Budget
from schemas.schemas import SchemaAddIncome, SchemaRemoveIncome

router = APIRouter()


@router.get('/budget')
def balance():
    result = Budget().balance()

    return result


@router.post('/budget/income')
def add_income_to_balance(schema: SchemaAddIncome):
    result = Budget().add_income_to_balance(schema)

    return result


@router.post('/budget/expense')
def remove_expense_from_balance(schema: SchemaRemoveIncome):
    result = Budget().add_expense_to_balance(schema)

    return result


@router.get('/budget/transactions')
def history_of_transactions():
    result = Budget().history_of_transactions()

    return result
