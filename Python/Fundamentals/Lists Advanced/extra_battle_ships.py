rows = int(input())
ships = [str(input()) for i in range(rows)]
ships = [[int(val) for ind, val in enumerate(rows) if val.isdigit()] for rows in ships]
attack_index = [[int(val) for ind, val in enumerate(attack) if val.isdigit()] for attack in str(input()).split()]

destroyed = 0

for i in attack_index:
    row = i[0]
    col = i[1]
    if row in range(len(ships)):
        if col in range(len(ships[row])):
            if ships[row][col] >= 1:
                ships[row][col] -= 1
                if ships[row][col] == 0:
                    destroyed += 1

print(destroyed)
