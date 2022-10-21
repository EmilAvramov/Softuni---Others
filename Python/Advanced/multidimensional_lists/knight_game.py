moves = {
    "up, left": [-2, -1],
    "up, right": [-2, 1],
    "down, left": [2, -1],
    "down, right": [2, 1],
    "left, up": [-1, -2],
    "left, down": [1, -2],
    "right, up": [-1, 2],
    "right, down": [1, 2],
}

rows = int(input())
matrix = [[i for i in input()] for _ in range(rows)]
cols = len(matrix[0])
knights = [0]


def check_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


def knights_positions():
    positions = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "K":
                positions.append(row)
                positions.append(col)
    return positions


while True:
    pos_knights = knights_positions()
    output = {}
    for i in range(0, len(pos_knights), 2):
        row, col = pos_knights[i], pos_knights[i + 1]
        for m_row, m_col in moves.values():
            knight_row, knight_col = row + m_row, col + m_col
            if check_valid_index(knight_row, knight_col):
                if matrix[knight_row][knight_col] == "K":
                    output[f"{row} {col}"] = output.get(f"{row} {col}", 0) + 1
    if sum(output.values()) == 0:
        break
    knights[0] += 1
    row, col = max(output, key=output.get).split()
    matrix[int(row)][int(col)] = "0"


print(knights[0])
