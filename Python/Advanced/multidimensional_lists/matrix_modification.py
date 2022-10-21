from collections import deque


rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(i) for i in input().split(" ")])

command = input()

while command != "END":
    tokens = deque(command.split(" "))
    action = tokens.popleft()
    [row, col, value] = [int(i) for i in tokens]

    if row < 0 or col < 0:
        print("Invalid coordinates")
    elif row > len(matrix) - 1:
        print("Invalid coordinates")
    elif col > len(matrix[0]) - 1:
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    command = input()

for row in matrix:
    print(" ".join(str(i) for i in row))
