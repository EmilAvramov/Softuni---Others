class Account:
    def __init__(self, _owner: str, _amount=0) -> None:
        self.owner = _owner
        self.amount = _amount
        self._transactions = []

    def add_transaction(self, _amount: int):
        if isinstance(_amount, int):
            self._transactions.append(_amount)
        else:
            raise ValueError("please use int for amount")

    @property
    def balance(self):
        result = 0
        result += self.amount
        for transaction in self._transactions:
            result += transaction
        return result

    def validate_transaction(self, _account, _amount_to_add: int):
        try:
            _account._transactions.append(_amount_to_add)
            if _account.balance < 0:
                raise ValueError("sorry cannot go in debt!")
        except ValueError:
            _account._transactions.pop()

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __add__(self, other):
        owner = f"{self.owner}&{other.owner}"
        amount = self.amount + other.amount
        new_account = Account(owner, amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    def __lt__(self, other):
        if self.balance < other.balance:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        else:
            return False

    def __le__(self, other):
        if self.balance <= other.balance:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.balance >= other.balance:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.balance == other.balance:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.balance != other.balance:
            return True
        else:
            return False
