import sys

[rows, columns] = [int(i) for i in input().split()]
matrix = []

for i in range(rows):
    matrix.append([int(i) for i in input().split()])

sub_matrix = []
sum_matrix = -sys.maxsize

for row in range(len(matrix) - 2):
    for column in range(len(matrix[0]) - 2):
        sub_sum = (
            matrix[row][column]
            + matrix[row][column + 1]
            + matrix[row][column + 2]
            + matrix[row + 1][column]
            + matrix[row + 1][column + 1]
            + matrix[row + 1][column + 2]
            + matrix[row + 2][column]
            + matrix[row + 2][column + 1]
            + matrix[row + 2][column + 2]
        )
        if sub_sum > sum_matrix:
            sum_matrix = sub_sum
            sub_matrix = [
                [
                    matrix[row][column],
                    matrix[row][column + 1],
                    matrix[row][column + 2],
                ],
                [
                    matrix[row + 1][column],
                    matrix[row + 1][column + 1],
                    matrix[row + 1][column + 2],
                ],
                [
                    matrix[row + 2][column],
                    matrix[row + 2][column + 1],
                    matrix[row + 2][column + 2],
                ],
            ]


print(f"Sum = {sum_matrix}")
if sub_matrix:
    for row in sub_matrix:
        print(" ".join([str(i) for i in row]))
