rows = int(input())
maze = [str(input()) for i in range(rows)]


def locate_path(_path):
    def check_location(_loc):
        location = []
        for row in _loc:
            if "k" in row:
                location.append(_loc.index(row))
                location.append(row.index('k'))
        return location

    def escape_route(_route):
        path = []
        for index_row, row in enumerate(_route):
            for index_col, col in enumerate(row):
                if col == " ":
                    path.append([index_row, index_col])
        return path

    kate_row = check_location(maze)[0]
    kate_col = check_location(maze)[1]


