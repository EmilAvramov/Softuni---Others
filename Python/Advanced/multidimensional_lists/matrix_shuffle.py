from collections import deque


[rows, cols] = [int(i) for i in input().split(" ")]
matrix = []

for i in range(rows):
    matrix.append([i for i in input().split(" ")])

command = input()

while command != "END":
    if "swap" not in command:
        print("Invalid input!")
    else:
        tokens = deque(command.split(" "))
        tokens.popleft()
        try:
            tokens = deque([int(x) for x in tokens])
            if len(tokens) != 4 or any([x < 0 for x in tokens]):
                print("Invalid input!")
            elif tokens[0] >= rows or tokens[2] >= rows:
                print("Invalid input!")
            elif tokens[1] >= cols or tokens[3] >= cols:
                print("Invalid input!")
            else:
                row1 = tokens[0]
                col1 = tokens[1]
                row2 = tokens[2]
                col2 = tokens[3]
                swap = matrix[row1][col1]
                matrix[row1][col1] = matrix[row2][col2]
                matrix[row2][col2] = swap
                for row in matrix:
                    print(" ".join([str(i) for i in row]))
        except:
            print("Invalid input!")

    command = input()
