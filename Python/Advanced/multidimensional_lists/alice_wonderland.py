def hole_end(alice: list, hole: list):
    if alice[0] == hole[0] and alice[1] == hole[1]:
        return True
    return False


def exit_end(alice: list, side: int):
    if 0 <= alice[0] < side and 0 <= alice[1] < side:
        return False
    return True


def tea_check(row: int, col: int, matrix: list):
    if matrix[row][col].isdigit():
        return True
    return False


side = int(input())
matrix = []

alice = [0, 0]
hole = [0, 0]
tea = 0
success = False

for i in range(side):
    row = [i for i in input().split(" ")]
    if "A" in row:
        alice = [i, row.index("A")]
    if "R" in row:
        hole = [i, row.index("R")]
    matrix.append(row)

matrix[alice[0]][alice[1]] = "*"

while True:
    command = input()
    if command == "down":
        alice[0] += 1
    elif command == "up":
        alice[0] -= 1
    elif command == "left":
        alice[1] -= 1
    elif command == "right":
        alice[1] += 1
    if hole_end(alice, hole):
        matrix[hole[0]][hole[1]] = "*"
        break
    if exit_end(alice, side):
        break
    if tea_check(alice[0], alice[1], matrix):
        tea += int(matrix[alice[0]][alice[1]])
    matrix[alice[0]][alice[1]] = "*"
    if tea >= 10:
        success = True
        break

if success:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in range(len(matrix)):
    print(" ".join(str(x) for x in matrix[row]))
