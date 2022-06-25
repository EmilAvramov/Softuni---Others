energy = int(input())
cmd = input()
won = 0
count = 0
is_lost = False

while cmd != "End of battle":
    if int(cmd) <= energy:
        energy -= int(cmd)
        won += 1
        count += 1
        if count % 3 == 0:
            energy += won
            count = 0
    else:
        is_lost = True
        break
    cmd = input()

if is_lost:
    print(
        f"Not enough energy! Game ends with {won} won battles and {energy} energy"
    )
else:
    print(f"Won battles: {won}. Energy left: {energy}")
