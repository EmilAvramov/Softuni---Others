class Account:
    def __init__(self, _id: int, _balance: int, _pin: int) -> None:
        self.__id = _id
        self.balance = _balance
        self.__pin = _pin

    def get_id(self, _pin: int):
        if _pin == self.__pin:
            return self.__id
        else:
            return "Wrong pin"

    def change_pin(self, _old_pin: int, _new_pin: int):
        if _old_pin == self.__pin:
            self.__pin = _new_pin
            return "Pin changed"
        else:
            return "Wrong pin"



account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
