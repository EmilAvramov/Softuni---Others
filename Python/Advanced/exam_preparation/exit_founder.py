def exit(player: str):
    return f"{player} found the Exit and wins the game!"


def trap(p1: str, p2: str):
    return f"{p1} is out of the game! The winner is {p2}."


def wall(player: str):
    return f"{player} hits a wall and needs to rest."


[p1, p2] = input().split(", ")
size = 6
matrix = []
skip_p1 = False
skip_p2 = False

for row in range(size):
    row = [i for i in input().split(" ")]
    matrix.append(row)

while True:
    [row_1, col_1] = [int(x) for x in input()[1:-1].split(", ")]

    if skip_p1 is False:
        if matrix[row_1][col_1] == "E":
            print(exit(p1))
            break
        if matrix[row_1][col_1] == "T":
            print(trap(p1, p2))
            break
        if matrix[row_1][col_1] == "W":
            print(wall(p1))
            skip_p1 = True
    else:
        skip_p1 = False

    [row_2, col_2] = [int(x) for x in input()[1:-1].split(", ")]
    if skip_p2 is False:
        if matrix[row_2][col_2] == "E":
            print(exit(p2))
            break
        if matrix[row_2][col_2] == "T":
            print(trap(p2, p1))
            break
        if matrix[row_2][col_2] == "W":
            print(wall(p2))
            skip_p2 = True
    else:
        skip_p2 = False
