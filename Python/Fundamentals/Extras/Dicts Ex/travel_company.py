vehicle_dict = {}
people_dict = {}

command = input()

while command != "ready":
    city = command.split(":")[0]
    vehicles = command.split(":")[1].split(",")
    vehicles = [i.split("-") for i in vehicles]
    vehicles = [
        [int(i) if i.isnumeric() else i for i in elem] for elem in vehicles
    ]
    for vehicle in vehicles:
        if city not in vehicle_dict.keys():
            vehicle_dict[city] = {vehicle[0]: vehicle[1]}
        else:
            vehicle_dict[city].update({vehicle[0]: vehicle[1]})
    command = input()

command = input()

while command != "travel time!":
    destination = command.split()[0]
    people = int(command.split()[1])
    people_dict[destination + str(people)] = {destination: people}
    command = input()

for key, value in people_dict.items():
    for sub_key, sub_value in value.items():
        if sum(vehicle_dict[sub_key].values()) >= sub_value:
            print(f"{sub_key} -> all {sub_value} accommodated")
        else:
            print(
                f"{sub_key} -> all except "
                f"{sub_value - sum(vehicle_dict[sub_key].values())} "
                f"accommodated"
            )
