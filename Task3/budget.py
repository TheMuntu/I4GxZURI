class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        final = 0
        for i in self.ledger:
            final += i["amount"]
        return final

    def transfer(self, amount, budget_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_cat.name}")
            budget_cat.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False


