class Cup:
    def __init__(self, _size: int, _quantity: int) -> None:
        self.size = _size
        self.quantity = _quantity

    def fill(self, _intake: int):
        if self.size - self.quantity >= _intake:
            self.quantity += _intake

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
