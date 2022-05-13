money = input()
balance = 0

while money != "NoMoreMoney":
    amount = float(money)
    if amount < 0:
        print(f'Invalid operation!')
        break
    else:
        print(f'Increase: {amount:.2f}')
        balance += amount
        money = input()

print(f'Total: {balance:.2f}')
