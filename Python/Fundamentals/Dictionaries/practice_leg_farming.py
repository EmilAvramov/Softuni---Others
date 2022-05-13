def check_qty(_item, _dict, _acquired):
    if _item in _dict.keys() and _dict[_item] >= 250:
        if _item == "shards":
            _acquired.append("Shadowmourne")
        elif _item == "fragments":
            _acquired.append("Valanyr")
        elif _item == "motes":
            _acquired.append("Dragonwrath")
        _dict[_item] -= 250
        return True


data = input().lower().split()
farming_dict = {}
item_acquired = []

stop_flag = False

while stop_flag is False:
    for i in range(0, len(data), 2):
        if data[i+1] not in farming_dict:
            farming_dict[data[i+1]] = int(data[i])
        else:
            farming_dict[data[i+1]] += int(data[i])
        if check_qty("shards", farming_dict, item_acquired):
            stop_flag = True
            break
        if check_qty("fragments", farming_dict, item_acquired):
            stop_flag = True
            break
        if check_qty("motes", farming_dict, item_acquired):
            stop_flag = True
            break
    if stop_flag:
        break
    data = input().lower().split()

print(f'{"".join(item_acquired)} obtained!')
print(f'shards: {farming_dict.get("shards", 0)}')
print(f'fragments: {farming_dict.get("fragments", 0)}')
print(f'motes: {farming_dict.get("motes",0)}')
for key, value in farming_dict.items():
    if key != "motes" and key != "fragments" and key != "shards":
        print(f'{key}: {value}')