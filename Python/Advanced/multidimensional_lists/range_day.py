from collections import deque


def check_space(player: list, matrix: list):
    if matrix[player[0]][player[1]] == ".":
        return True
    return False


def check_move(player: list):
    if 0 <= player[0] < 5 and 0 <= player[1] < 5:
        return True
    return False


matrix = []
player = [0, 0]
targets = []
shot = []


for i in range(5):
    row = [i for i in input().split(" ")]
    if "A" in row:
        player = [i, row.index("A")]
    if "x" in row:
        found = [i for i, v in enumerate(row) if v == "x"]
        for index in range(len(found)):
            targets.append([i, found[index]])
    matrix.append(row)

total_targets = [sum([matrix[row].count("x") for row in range(5)])]
matrix[player[0]][player[1]] = "."


def shoot(target: list):
    matrix[target[0]][target[1]] = "."
    shot.append(target)
    targets.remove(target)


commands = int(input())

for i in range(commands):
    tokens = deque([i for i in input().split(" ")])
    command = tokens.popleft()
    if command == "move":
        direction = tokens.popleft()
        steps = int(tokens.popleft())
        if direction == "right":
            moved = [player[0], player[1] + steps]
        elif direction == "left":
            moved = [player[0], player[1] - steps]
        elif direction == "up":
            moved = [player[0] - steps, player[1]]
        else:  # down
            moved = [player[0] + steps, player[1]]
        if check_move(moved):
            if check_space(moved, matrix):
                player = moved
    else:
        direction = tokens.popleft()
        if direction == "right":
            for target in targets:
                if player[0] == target[0] and player[1] < target[1]:
                    shoot(target)
                    break
        elif direction == "left":
            for target in targets:
                if player[0] == target[0] and player[1] > target[1]:
                    shoot(target)
                    break
        elif direction == "up":
            for target in targets:
                if player[1] == target[1] and player[0] > target[0]:
                    shoot(target)
                    break
        else:  # down
            for target in targets:
                if player[1] == target[1] and player[0] < target[0]:
                    shoot(target)
                    break

if total_targets[0] == len(shot):
    print(f"Training completed! All {len(shot)} targets hit.")
else:
    print(
        f"Training not completed! {total_targets[0] - len(shot)} targets left."
    )
for item in shot:
    print(f"{item}")
