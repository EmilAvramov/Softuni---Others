lines = int(input())

color_dict = {}
dup_inventory = {}

for line in range(lines):
    color_clothes = input().split(' -> ')
    color = color_clothes[0]
    clothes = color_clothes[1].split(',')
    for item in clothes:
        if color + item not in dup_inventory.keys():
            dup_inventory[color + item] = 1
        else:
            dup_inventory[color + item] += 1
    if color not in color_dict.keys():
        color_dict[color] = [clothes[0]]
        for i in range(1, len(clothes)):
            if clothes[i] not in color_dict[color]:
                color_dict[color].append(clothes[i])
    else:
        for i in range(len(clothes)):
            if clothes[i] not in color_dict[color]:
                color_dict[color].append(clothes[i])

search = input().split()

for key, value in color_dict.items():
    print(f"{key} clothes:", end='\n')
    for clothes in value:
        if key == search[0] and clothes == search[1]:
            print(f"* {clothes} - {dup_inventory[key + clothes]} (found!)")
        else:
            print(f"* {clothes} - {dup_inventory[key + clothes]}")

