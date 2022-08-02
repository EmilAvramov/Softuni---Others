count = int(input())
plant_dict = {}

for i in range(count):
    [plant, rarity] = input().split("<->")
    plant_dict[plant] = [rarity, []]

command = input()

while command != "Exhibition":
    cmd = command.split(": ")[0]
    data = command.split(": ")[1]

    if "Reset" in cmd:
        plant = data
        if plant not in plant_dict.keys():
            print("error")
        else:
            plant_dict[plant][1] = []
    else:
        [plant, value] = data.split(" - ")
        if plant not in plant_dict.keys():
            print("error")
        else:
            if "Rate" in cmd:
                plant_dict[plant][1].append(int(value))
            elif "Update" in cmd:
                plant_dict[plant][0] = int(value)
    command = input()

print("Plants for the exhibition:")
for [plant, data] in plant_dict.items():
    if len(data[1]) > 0:
        print(
            f"- {plant}; Rarity: {data[0]}; Rating: {(sum([x for x in data[1]])/len(data[1])):.2f}"
        )
    else:
        print(f"- {plant}; Rarity: {data[0]}; Rating: 0.00")
