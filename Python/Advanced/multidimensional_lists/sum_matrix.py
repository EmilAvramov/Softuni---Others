[rows, columns] = [int(i) for i in input().split(", ")]
matrix = []
sum_digits = 0

for i in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

for i in range(rows):
    for j in range(columns):
        sum_digits += matrix[i][j]

print(sum_digits)
print(matrix)
