size = int(input())
matrix = []
diagonal_sum = 0

for i in range(size):
    matrix.append([int(i) for i in input().split()])

for row in range(len(matrix)):
    diagonal_sum += matrix[row][row]

print(diagonal_sum)
