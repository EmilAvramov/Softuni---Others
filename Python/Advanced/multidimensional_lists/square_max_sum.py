import sys

[row, column] = [int(i) for i in input().split(", ")]
matrix = []
sub_matrix = []
max_sum = -sys.maxsize

for i in range(row):
    matrix.append([int(i) for i in input().split(", ")])

for row in range(row - 1):
    for column in range(len(matrix[row]) - 1):
        temp_sum = (
            matrix[row][column]
            + matrix[row][column + 1]
            + matrix[row + 1][column]
            + matrix[row + 1][column + 1]
        )
        if temp_sum > max_sum:
            max_sum = temp_sum
            sub_matrix = [
                [matrix[row][column], matrix[row][column + 1]],
                [matrix[row + 1][column], matrix[row + 1][column + 1]],
            ]


for row in range(len(sub_matrix)):
    print(" ".join([str(i) for i in sub_matrix[row]]))
print(max_sum)
