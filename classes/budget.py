from functions.file_manager import read_file, update_file


class Budget(object):

    def __init__(self):
        self.budget = read_file()

    def balance(self):

        return {'balance': self.budget["balance"]}

    def add_income_to_balance(self, data):

        if data.description != '':
            self.budget['history'].append({'description': data.description, 'amount': data.amount, 'type': 'income'})
            self.budget["balance"] += data.amount
            update_file(self.budget)
            return {"description": data.description, "amount": data.amount}
        else:
            return {"Error": "description is empty"}

    def add_expense_to_balance(self, data):

        if data.description != '' and self.budget['balance'] >= data.amount:
            self.budget['history'].append({'description': data.description, 'amount': data.amount, 'type': 'expense'})
            self.budget["balance"] -= data.amount

            update_file(self.budget)
            return {"description": data.description, "amount": data.amount}
        else:
            return {"Error": "description is empty or not enough balance"}

    def history_of_transactions(self):
        expense_transactions = []
        income_transactions = []
        for transaction in self.budget['history']:
            if transaction['type'] == 'expense':
                expense_transactions.append(transaction)
            else:
                income_transactions.append(transaction)

        return {'expenses': expense_transactions, 'incomes': income_transactions}
