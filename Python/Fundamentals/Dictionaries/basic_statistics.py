new_item = input().split(":")
inventory = {}

while new_item[0] != "statistics":
    key = new_item[0]
    value = int(new_item[1])
    if key not in inventory:
        inventory[key] = value
    else:
        inventory[key] += value
    new_item = input().split(":")

print("Products in stock:")
for key, value in inventory.items():
    print(f"- {key}: {value}", end="\n")
print(f"Total Products: {len(inventory)}")
print(f"Total Quantity: {sum(inventory.values())}")
