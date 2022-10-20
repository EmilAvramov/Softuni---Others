from collections import deque

materials = deque([int(i) for i in input().split(" ")])
levels = deque([int(i) for i in input().split(" ")])
success = False

inventory = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}
crafted = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while len(materials) > 0 and len(levels) > 0:
    material = materials[-1]
    level = levels[0]
    result = material * level

    for key, value in inventory.items():
        if value == result:
            crafted[key] += 1
            materials.pop()
            levels.popleft()
            break

    if result < 0:
        result = material + level
        materials.pop()
        levels.popleft()
        materials.append(result)
    elif result > 0 and result not in inventory.values():
        levels.popleft()
        materials[-1] += 15
    else:
        if material == 0:
            materials.pop()
        if level == 0:
            levels.popleft()
    if crafted["Doll"] >= 1 and crafted["Wooden train"] >= 1:
        success = True
    if crafted["Teddy bear"] >= 1 and crafted["Bicycle"] >= 1:
        success = True

materials_new = deque([])
for item in materials:
    materials_new.appendleft(item)

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if len(materials) > 0:
    print(f"Materials left: {', '.join(str(x) for x in materials_new)}")
if len(levels) > 0:
    print(f"Magic left: {', '.join(str(x) for x in levels)}")

for key, value in sorted(crafted.items(), key=lambda x: x[0]):
    if value > 0:
        print(f"{key}: {value}")
