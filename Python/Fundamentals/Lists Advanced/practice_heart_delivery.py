area = [int(i) for i in str(input()).split('@')]
cmd = str(input()).split()

index = 0
success_counter = 0

while cmd[0] != "Love!":
    step = int(cmd[1])

    if step + index >= len(area):
        index = 0
    else:
        index = step + index

    if cmd[0] == "Jump":
        if area[index] <= 0:
            print(f"Place {index} already had Valentine's day.")
            area[index] = 0
        else:
            area[index] -= 2
            if area[index] <= 0:
                print(f"Place {index} has Valentine's day.")
                success_counter += 1
    cmd = str(input()).split()

print(f"Cupid's last position was {index}.")
if success_counter == len(area):
    print(f'Mission was successful.')
else:
    print(f'Cupid has failed {len(area) - success_counter} places.')