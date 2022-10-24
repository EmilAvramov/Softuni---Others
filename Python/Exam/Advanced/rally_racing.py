size = int(input())
racer = input()

matrix = []
car = [0, 0]
tunnels = []
finish = ""
kms = 0
failed = False
success = False

for row in range(size):
    data = [i for i in input().split(" ")]
    if "T" in data:
        found = [i for i, v in enumerate(data) if v == "T"]
        for index in found:
            tunnels.append([row, index])
    if "F" in data:
        finish = [row, data.index("F")]
    matrix.append(data)

matrix[0][0] = "C"
command = input()

while True:
    if command == "End":
        if success is False:
            failed = True
        break
    if success is False:
        if command == "left":
            moved = [car[0], car[1] - 1]
        elif command == "right":
            moved = [car[0], car[1] + 1]
        elif command == "up":
            moved = [car[0] - 1, car[1]]
        else:  # down
            moved = [car[0] + 1, car[1]]
        if matrix[moved[0]][moved[1]] == "F":
            matrix[moved[0]][moved[1]] = "C"
            kms += 10
            success = True
        elif matrix[moved[0]][moved[1]] == "T":
            if tunnels[0] == moved:
                moved = tunnels[1]
                matrix[tunnels[0][0]][tunnels[0][1]] = "."
                matrix[tunnels[1][0]][tunnels[1][1]] = "C"
            else:
                moved = tunnels[0]
                matrix[tunnels[1][0]][tunnels[1][1]] = "."
                matrix[tunnels[0][0]][tunnels[0][1]] = "C"
            kms += 30
        else:
            kms += 10
            matrix[moved[0]][moved[1]] = "C"
        matrix[car[0]][car[1]] = "."
        car = moved
    command = input()

if success:
    print(f"Racing car {racer} finished the stage!")
if failed:
    print(f"Racing car {racer} DNF.")
print(f"Distance covered {kms} km.")
for row in matrix:
    print("".join(row))
