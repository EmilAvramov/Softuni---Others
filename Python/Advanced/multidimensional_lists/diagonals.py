rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

primary_diag_sum = sum([matrix[i][i] for i in range(len(matrix))])
primary_diag_symbols = [matrix[i][i] for i in range(len(matrix))]

secondary_diag_sum = sum(
    [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
)
secondary_diag_symbols = [
    matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))
]

print(
    f"Primary diagonal: {', '.join([str(i) for i in primary_diag_symbols])}. Sum: {primary_diag_sum}"
)
print(
    f"Secondary diagonal: {', '.join([str(i) for i in secondary_diag_symbols])}. Sum: {secondary_diag_sum}"
)
