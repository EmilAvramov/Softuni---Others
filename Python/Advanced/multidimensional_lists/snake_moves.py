from collections import deque


[rows, cols] = [int(i) for i in input().split(" ")]
snake = input()
index = 0

for row in range(rows):
    matrix_row = deque()
    for col in range(cols):
        if index == len(snake):
            index = 0
        if row % 2 == 0:
            matrix_row.append(snake[index])
        else:
            matrix_row.appendleft(snake[index])
        index += 1
    print("".join(matrix_row))

# for i in range(rows):
#     sub = []
#     index = 0
#     for char in last:
#         sub.append(char)
#         index = snake.index(char)
#     mid = snake[index + 1 : cols + 1]
#     last = mid + snake[: (cols - len(mid))]
#     if i % 2 == 0:
#         matrix.append(sub)
#     else:
#         matrix.append(reversed(sub))

# for row in range(len(matrix)):
#     print("".join(str(x) for x in matrix[row]))