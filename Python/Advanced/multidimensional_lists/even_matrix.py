rows = int(input())
matrix = []

for i in range(rows):
    data = [int(i) for i in input().split(", ")]
    matrix.append([i for i in data if i % 2 == 0])

print(matrix)
