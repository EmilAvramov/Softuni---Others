from collections import deque


def check_space(player: list, matrix: list):
    if matrix[player[0]][player[1]] == ".":
        return True
    return False


def check_move(player: list, matrix: list):
    if player[0] >= 0 and player[0] < len(matrix):
        if player[1] >= 0 and player[1] < len(matrix[0]):
            return True
        return False
    return False


matrix = []
player = [0, 0]
targets = []

for i in range(5):
    row = [i for i in input().split(" ")]
    if "A" in row:
        player = [i, row.index("A")]
    if "x" in row:
        targets.append([i, row.index("x")])
    matrix.append(row)

commands = int(input())

for i in range(commands):
    tokens = deque([i for i in input().split(" ")])
    command = deque.popleft()
    if command == "move":
        direction = tokens.popleft()
        steps = tokens.popleft()
        if direction == "right":
            moved = [player[0], player[1] + 1]
        elif direction == "left":
            moved = [player[0], player[1] - 1]
        elif direction == "up":
            moved = [player[0] - 1, player[1]]
        else:  # down
            moved = [player[0] + 1, player[1]]
        if check_move(moved, matrix):
            if check_space(moved, matrix):
                player = moved
    else:
        steps = tokens.popleft()
