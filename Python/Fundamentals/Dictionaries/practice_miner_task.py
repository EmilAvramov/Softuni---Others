resource = input()
inventory = {}

while resource != "stop":
    amount = int(input())
    if resource not in inventory:
        inventory[resource] = amount
    else:
        inventory[resource] += amount
    resource = input()

for key, value in inventory.items():
    print(f'{key} -> {value}')