command = input().split(" ")

product_dict = {}

while command[0] != "exam":
    if command[0] == "shopping":
        command = input().split(" ")
        continue
    action = command[0]
    product = command[1]
    quantity = int(command[2])
    if action == "stock":
        if product in product_dict.keys():
            product_dict[product] += quantity
        else:
            product_dict[product] = quantity
    else:
        if product not in product_dict.keys():
            print(f"{product} doesn't exist")
        elif product in product_dict.keys() and product_dict[product] == 0:
            print(f"{product} out of stock")
        elif product in product_dict.keys() and quantity > product_dict[product]:
            product_dict[product] = 0
        else:
            product_dict[product] -= quantity
    command = input().split(" ")

for key, value in product_dict.items():
    if value > 0:
        print(f"{key} -> {value}")

