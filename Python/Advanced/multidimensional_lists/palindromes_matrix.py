[rows, columns] = [int(i) for i in input().split()]
matrix = []

for row in range(rows):
    symbols = []
    for column in range(columns):
        symbols.append(chr(97 + row) + chr(97 + row + column) + chr(97 + row))
    matrix.append(symbols)

for row in matrix:
    print(" ".join(row))
