[rows, columns] = [int(i) for i in input().split()]
matrix = []

for i in range(rows):
    matrix.append([i for i in input().split(" ")])

squares_count = 0

for row in range(len(matrix) - 1):
    for column in range(len(matrix[0]) - 1):
        if (
            matrix[row][column]
            == matrix[row + 1][column]
            == matrix[row][column + 1]
            == matrix[row + 1][column + 1]
        ):
            squares_count += 1

print(squares_count)
