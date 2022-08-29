# Bank account object

class Bank_Account:
    """Hold information about bank account"""

    def __init__(self, _first_name: str, _last_name: str, _account_number: int, _balance: float):
        """init function"""

        self.first_name = _first_name
        self.last_name = _last_name
        self.account_number = _account_number
        self.balance = _balance

        self.transactions = []
        if _balance < 0:
            self.is_debt = True
        else:
            self.is_debt = False

    def __str__(self):
        """print status of bank"""
        return f'Name: {self.first_name} {self.last_name}, Account number: {self.account_number}, Balance: {self.balance}'

    def withdraw(self, amount: int):
        """withdraw from account"""

        if self.balance >= amount >= 0:
            self.balance -= amount
            self.transactions.append(-amount)
        else:
            self.balance -= amount
            self.transactions.append(-amount)
            self.is_debt = True

    def deposit(self, amount: int):
        """deposit from account"""

        if amount >= 0:
            self.balance += amount
            self.transactions.append(amount)


# == main ==
if __name__ == "__main__":
    my_account = Bank_Account("Oriel", "Naim", 1, 1500)
    my_account.deposit(600)
    my_account.withdraw(2100)
    print(my_account.transections)
    print(my_account.is_debt)
