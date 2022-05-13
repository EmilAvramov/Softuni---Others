class BankAccount:

    def __init__(self, name: str, bank: str, balance: float):
        self.name = name
        self.bank = bank
        self.balance = balance

    def unpack_self(self):
        return [self.name, [self.bank, self.balance]]


data = input()
storage = {}

while data != "end":
    bank_name = data.split(" | ")[0]
    account_name = data.split(" | ")[1]
    account_balance = float(data.split(" | ")[2])
    account = BankAccount(account_name, bank_name,
                          account_balance).unpack_self()
    if account[0] not in storage.keys():
        storage[account[0]] = {account[1][0]: account[1][1]}
    else:
        storage[account[0]].update({account[1][0]: account[1][1]})
    data = input()

for key, value in sorted(storage.items(),
                         key=lambda x: sum(x[1].values()), reverse=True):
    for sub_key, sub_value in sorted(value.items(),
                                     key=lambda x: len(x[0])):
        print(f"{key} -> ", end='')
        print(f"{sub_value:.2f} ({sub_key})")
