command = input().split()

inventory_qty = {}
inventory_prices = {}
result_inventory = {}

while command[0] != "buy":
    operation = command[0]
    price = float(command[1])
    qty = int(command[2])
    if operation not in inventory_qty:
        inventory_qty[operation] = qty
        inventory_prices[operation] = price
    else:
        inventory_qty[operation] += qty
        inventory_prices[operation] = price
    command = input().split()

result_inventory = {
    k: inventory_prices[k] * inventory_qty[k] for k in inventory_prices
}
for key, value in result_inventory.items():
    print(f"{key} -> {value:.2f}")
