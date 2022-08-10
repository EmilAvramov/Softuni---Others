size = int(input())
matrix = []

for i in range(size):
    matrix.append([int(i) for i in input().split()])

primary_diag_sum = sum([matrix[i][i] for i in range(len(matrix))])
secondary_diag_sum = sum(
    [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
)

print(abs(primary_diag_sum - secondary_diag_sum))
