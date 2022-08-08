size = int(input())
matrix = []

for i in range(size):
    matrix.append([i for i in input()])

symbol = input()
match = ""

for row in range(len(matrix)):
    for column in range(len(matrix)):
        if matrix[row][column] == symbol:
            match = (row, column)

if match:
    print(match)
else:
    print(f"{symbol} does not occur in the matrix")
