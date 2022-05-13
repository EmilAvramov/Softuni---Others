items = input().split(" = ")

items_dict = {}

while items[0] != "end":
    if items[1] not in items_dict.keys() and items[1].isnumeric():
        items_dict[items[0]] = items[1]
    elif items[1] in items_dict.keys():
        items_dict[items[0]] = items_dict[items[1]]
    items = input().split(" = ")

for key, value in items_dict.items():
    print(f'{key} === {int(value)}')
