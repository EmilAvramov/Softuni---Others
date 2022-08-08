[rows, columns] = [int(i) for i in input().split(", ")]
matrix = []

for i in range(rows):
    matrix.append([int(i) for i in input().split()])

for column in range(len(matrix[0])):
    total = 0
    for row in matrix:
        total += row[column]
    print(total)
