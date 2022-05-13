class Account:
    def __init__(self, _id: int, _name: str, _balance=0) -> None:
        self.id = _id
        self.name = _name
        self.balance = _balance

    def credit(self, _amount: int):
        self.balance += _amount
        return self.balance

    def debit(self, _amount: int):
        if _amount <= self.balance:
            self.balance -= _amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self):
        return (
            f"User {self.name} with account {self.id} has "
            f"{self.balance} balance"
        )


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
