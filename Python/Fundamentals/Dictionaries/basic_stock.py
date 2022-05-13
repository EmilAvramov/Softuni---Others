dict_items = input().split()
search = input().split()
inventory = {}

for i in range(0, len(dict_items), 2):
    key = dict_items[i]
    value = dict_items[i + 1]
    inventory[key] = int(value)

for product in search:
    if product in inventory:
        print(f'We have {inventory[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
