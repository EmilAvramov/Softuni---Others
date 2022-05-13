destination = str(input())
needed_money = float(input())

saved_money = 0

while destination != "End":
    amount = float(input())
    saved_money += amount
    if saved_money >= needed_money:
        print(f'Going to {destination}!')
        saved_money = 0
        destination = str(input())
        if destination == "End":
            break
        needed_money = float(input())
