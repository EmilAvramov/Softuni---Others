def check_index(santa: list, size: int):
    if 0 <= santa[0] < size and 0 <= santa[1] < size:
        return True
    return False


def check_visit(santa: list, matrix: list):
    if matrix[santa[0]][santa[1]] == "V":
        return True
    return False


def check_kid(santa: list, matrix: list):
    if matrix[santa[0]][santa[1]] == "X" or matrix[santa[0]][santa[1]] == "V":
        return True
    return False


def eat_cookie(santa: list, matrix: list, presents: int):
    good = 0
    total = 0
    santa_north = [santa[0] - 1, santa[1]]
    santa_south = [santa[0] + 1, santa[1]]
    santa_west = [santa[0], santa[1] - 1]
    santa_east = [santa[0], santa[1] + 1]
    if check_kid(santa_north, matrix):
        if check_visit(santa_north, matrix):
            good += 1
        total += 1
        presents -= 1
        matrix[santa_north[0]][santa_north[1]] = "-"
        if presents == 0:
            return [good, total, matrix]
    if check_kid(santa_south, matrix):
        if check_visit(santa_south, matrix):
            good += 1
        total += 1
        presents -= 1
        matrix[santa_south[0]][santa_south[1]] = "-"
        if presents == 0:
            return [good, total, matrix]
    if check_kid(santa_west, matrix):
        if check_visit(santa_west, matrix):
            good += 1
        total += 1
        presents -= 1
        matrix[santa_west[0]][santa_west[1]] = "-"
        if presents == 0:
            return [good, total, matrix]
    if check_kid(santa_east, matrix):
        if check_visit(santa_east, matrix):
            good += 1
        total += 1
        presents -= 1
        matrix[santa_east[0]][santa_east[1]] = "-"
        if presents == 0:
            return [good, total, matrix]
    return [good, total, matrix]


presents: int = int(input())
size: int = int(input())

matrix: list = []
santa: list = [0, 0]
nice: list = []
given: int = 0

for i in range(size):
    row = [i for i in input().split(" ")]
    if "S" in row:
        santa = [i, row.index("S")]
    if "V" in row:
        indices = [i for i, v in enumerate(row) if v == "V"]
        for index in indices:
            nice.append([i, index])
    matrix.append(row)

command = input()

while command != "Christmas morning":
    if command == "up":
        moved = [santa[0] - 1, santa[1]]
    elif command == "down":
        moved = [santa[0] + 1, santa[1]]
    elif command == "left":
        moved = [santa[0], santa[1] - 1]
    else:  # right
        moved = [santa[0], santa[1] + 1]
    if check_index(moved, size):
        if check_visit(moved, matrix):
            presents -= 1
            given += 1
        else:
            if matrix[moved[0]][moved[1]] == "C":
                [good, total, newMatrix] = eat_cookie(moved, matrix, presents)
                matrix = newMatrix
                given += good
                presents -= total
        matrix[santa[0]][santa[1]] = "-"
        santa = moved
        matrix[santa[0]][santa[1]] = "S"
    if presents == 0:
        break
    command = input()

if given < len(nice):
    print("Santa ran out of presents!")

[print(*matrix[row]) for row in range(size)]

if given < len(nice):
    print(f"No presents for {len(nice) - given} nice kid/s.")
else:
    print(f"Good job, Santa! {given} happy nice kid/s.")
