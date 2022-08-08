rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

matrix = [i for elem in matrix for i in elem]

print(matrix)
