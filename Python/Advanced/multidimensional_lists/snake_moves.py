[rows, cols] = [int(i) for i in input().split(" ")]
snake = input()
matrix = []
index = 0

for i in range(rows):
    if i % 2 == 0:
        for j in range(cols):
            matrix.append(snake[0:cols])
            print(index)
            break
    else:
        for j in range(cols):
            matrix.append(snake[cols::-1])
            break

for row in range(len(matrix)):
    print("".join(str(x) for x in matrix[row]))
