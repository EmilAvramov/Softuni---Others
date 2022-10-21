# def check_direction(row: list, direction: str):
#     count = 0
#     index = row.index("B")
#     indices = []
#     for i in range(len(row)):
#         if row[i] == "B":
#             for sub in row[index + 1 :]:
#                 if sub != "X":
#                     count += int(sub)
#                     indices.append([i, row.index(sub)])
#                 else:
#                     break
#     return [count, indices, direction]


# rows = int(input())
# matrix = []
# bunny_index_row = ""
# bunny_index_col = ""
# eggs = 0
# bunny_row = []
# bunny_col = []

# for row in range(rows):
#     fields = [i for i in input().split(" ")]
#     if "B" in fields:
#         bunny_index_row = row
#         bunny_index_col = fields.index("B")
#         bunny_row = fields
#     matrix.append(fields)

# cols = len(matrix[0])

# for row in range(len(matrix)):
#     for col in range(cols):
#         if col == bunny_index_col:
#             bunny_col.append(matrix[row][col])

# right = check_direction(bunny_row, "right")
# for item in right[1]:
#     item[0] = bunny_index_row

# bunny_row = bunny_row[::-1]

# left = check_direction(bunny_row, "left")
# for item in left[1]:
#     item[0] = bunny_index_row

# down = check_direction(bunny_col, "down")
# for item in down[1]:
#     item[0] = bunny_index_col
#     item[0], item[1] = item[1], item[0]

# bunny_col = bunny_col[::-1]

# up = check_direction(bunny_col, "up")
# for item in up[1]:
#     item[0] = bunny_index_col

# eggs = max(right, left, up, down)

# print(eggs[2])
# for item in eggs[1]:
#     print(item)
# print(eggs[0])

n = int(input())
matrix = []
bunny_i = 0
bunny_j = 0

# 1) traverse the matrix and find the Bunny's location; keep the Bunny's coordinates:
for i in range(n):
    line = input().split()
    matrix.append(line)
    # check the location of the bunny
    for j in range(n):
        if line[j] == "B":
            bunny_i = i
            bunny_j = j

# 2) explore every possible route - we have four possible routes - up, down, left, right:
possible_route = ["up", "down", "left", "right"]
best_direction = ""
best_path = []
best_score = float("-inf")

for x in possible_route:
    current_row, current_col = bunny_i, bunny_j
    bunny_path = []
    current_score = 0

    # try to move up:
    if x == "up":
        while True:
            current_row, current_col = current_row - 1, current_col
            if (
                current_row < 0
                or current_col < 0
                or current_row >= n
                or current_col >= n
                or matrix[current_row][current_col] == "X"
            ):
                break
            else:
                bunny_path.append([current_row, current_col])
                current_score += int(matrix[current_row][current_col])
            if current_score > best_score and bunny_path:
                best_score = current_score
                best_direction = "up"
                best_path = bunny_path

    # try to move down:
    if x == "down":
        while True:
            current_row, current_col = current_row + 1, current_col
            if (
                current_row < 0
                or current_col < 0
                or current_row >= n
                or current_col >= n
                or matrix[current_row][current_col] == "X"
            ):
                break
            else:
                bunny_path.append([current_row, current_col])
                current_score += int(matrix[current_row][current_col])
            if current_score > best_score and bunny_path:
                best_score = current_score
                best_direction = "down"
                best_path = bunny_path

    # try to move left:
    if x == "left":
        while True:
            current_row, current_col = current_row, current_col - 1
            if (
                current_row < 0
                or current_col < 0
                or current_row >= n
                or current_col >= n
                or matrix[current_row][current_col] == "X"
            ):
                break
            else:
                bunny_path.append([current_row, current_col])
                current_score += int(matrix[current_row][current_col])
            if current_score > best_score and bunny_path:
                best_score = current_score
                best_direction = "left"
                best_path = bunny_path

    # try to move right:
    if x == "right":
        while True:
            current_row, current_col = current_row, current_col + 1
            if (
                current_row < 0
                or current_col < 0
                or current_row >= n
                or current_col >= n
                or matrix[current_row][current_col] == "X"
            ):
                break
            else:
                bunny_path.append([current_row, current_col])
                current_score += int(matrix[current_row][current_col])
            if current_score > best_score and bunny_path:
                best_score = current_score
                best_direction = "right"
                best_path = bunny_path

print(best_direction)
for x in best_path:
    print(x)
print(best_score)
