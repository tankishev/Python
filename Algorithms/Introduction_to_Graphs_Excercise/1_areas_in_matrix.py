def dfs(r, c, matrix, visited, component):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        return 0
    if visited[r][c] or matrix[r][c] == '*':
        return 0
    component.append((r, c))
    visited[r][c] = True
    dfs(r - 1, c, matrix, visited, component)
    dfs(r + 1, c, matrix, visited, component)
    dfs(r, c - 1, matrix, visited, component)
    dfs(r, c + 1, matrix, visited, component)
    return component


def solution():
    rows = int(input())
    cols = int(input())
    matrix = [[ch for ch in input()] for _ in range(rows)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    areas = []
    for r in range(rows):
        for c in range(cols):
            if visited[r][c] or matrix[r][c] == '*':
                continue
            areas.append(dfs(r, c, matrix, visited, []))

    areas.sort(key=lambda el: (-len(el), el[0]))
    print(f'Total areas found: {len(areas)}')
    for i, area in enumerate(areas):
        r, c = area[0]
        print(f'Area #{i + 1} at ({r}, {c}), size: {len(area)}')


if __name__ == '__main__':
    solution()
