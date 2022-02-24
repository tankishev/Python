# Create a class called Account. Upon initialization, it should receive an id (number), a name (string), and a balance
# (integer; optional; 0 by default). The class should also have 3 additional instance methods:
# -	credit(amount) - adds the amount to the balance and returns the new balance
# -	debit(amount) - if the amount is less than or equal to the balance, reduces the balance by the amount and returns
# the new balance. Otherwise, return "Amount exceeded balance"
# -	info() - returns "User {name} with account {id} has {balance} balance"


class Account:

    def __init__(self, id_: int, name: str, *balance: int):
        self.id = id_
        self.name = name
        self.balance = balance[0] if balance else 0

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> any:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return 'Amount exceeded balance'

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
