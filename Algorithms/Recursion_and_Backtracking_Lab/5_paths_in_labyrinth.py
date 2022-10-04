def is_valid(cell: tuple) -> bool:
    r, c = cell
    return 0 <= r < rows and 0 <= c < cols and labyrinth[r][c] != '*'


def is_exit(cell: tuple) -> bool:
    r, c = cell
    return labyrinth[r][c] == 'e'


def find_paths(cell=(0, 0), direction='', visited=None, path=None):
    if visited is None:
        visited = []
    visited.append(cell)
    if path is None:
        path = []
    path.append(direction)

    if is_exit(cell):
        print(*path, sep='')
        return

    possible_routes = [k for k, v in directions.items() if is_valid(v(cell)) and v(cell) not in visited]

    if not possible_routes:
        return

    for route in possible_routes:
        next_cell = directions[route](cell)
        find_paths(next_cell, route, visited, path)
        visited.pop()
        path.pop()


directions = {
    'U': lambda x: (x[0] - 1, x[1]),
    'D': lambda x: (x[0] + 1, x[1]),
    'L': lambda x: (x[0], x[1] - 1),
    'R': lambda x: (x[0], x[1] + 1)
}

rows = int(input())
cols = int(input())
labyrinth = [[el for el in input()] for r in range(rows)]
find_paths()
