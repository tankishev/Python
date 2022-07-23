moves = {
    'up': lambda c: (c[0] - 1, c[1]),
    'down': lambda c: (c[0] + 1, c[1]),
    'left': lambda c: (c[0], c[1] - 1),
    'right': lambda c: (c[0], c[1] + 1)
}


def get_cell(cell, matrix):
    r, c = cell
    if min(r, c) < 0 or r >= len(matrix) or c >= len(matrix[0]):
        return None
    return matrix[r][c]


def get_adjacent(cell, matrix) -> list:
    retval = []
    r, c = cell
    val = matrix[r][c]
    for move in moves.values():
        next_cell = move(cell)
        if get_cell(next_cell, matrix) == val:
            retval.append(next_cell)
    return retval


def get_components(graph: dict) -> list:
    unprocessed = [el for el in graph.keys()]
    components = []
    while unprocessed:
        component = dfs(unprocessed[0],graph)
        components.append(component)
        unprocessed = [x for x in unprocessed if x not in component]

    return components


def dfs(node: int, graph: dict, component=None, visited=None):
    if visited is None:
        visited = []
    if component is None:
        component = []

    if node in visited:
        return
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child, graph, component, visited)
    if node not in component:
        component.append(node)
    return component


def solution():
    rows = int(input())
    cols = int(input())
    matrix = [[ch for ch in input()] for _ in range(rows)]

    graph = {}
    for r in range(rows):
        for c in range(cols):
            cell = (r, c)
            graph[cell] = get_adjacent(cell, matrix)

    components = get_components(graph)
    summary = {}
    for component in components:
        letter = get_cell(component[0], matrix)
        if letter not in summary:
            summary[letter] = 0
        summary[letter] += 1

    summary = {k: v for k, v in sorted(summary.items(), key=lambda item: item[0])}
    print(f'Areas: {len(components)}')
    for k, v in summary.items():
        print(f"Letter '{k}' -> {v}")


if __name__ == '__main__':
    solution()