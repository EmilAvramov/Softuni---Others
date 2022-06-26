route = input().split("||")
fuel = int(input())
ammo = int(input())
mission = True

for item in route:
    try:
        cmd = item.split(" ")[0]
        value = int(item.split(" ")[1])
        if cmd == "Travel":
            if fuel >= value:
                fuel -= value
                print(f"The spaceship travelled {value} light-years.")
            else:
                print("Mission failed.")
                mission = False
                break
        elif cmd == "Enemy":
            if ammo >= value:
                ammo -= value
                print(f"An enemy with {value} armour is defeated.")
            else:
                if fuel >= value * 2:
                    fuel -= value * 2
                    print(f"An enemy with {value} armour is outmaneuvered.")
                else:
                    print("Mission failed.")
                    mission = False
                    break
        elif cmd == "Repair":
            fuel += value
            ammo += value * 2
            print(f"Ammunitions added: {value * 2}.")
            print(f"Fuel added: {value}.")
    except IndexError:
        print("You have reached Titan, all passengers are safe.")
        mission = True
        break
