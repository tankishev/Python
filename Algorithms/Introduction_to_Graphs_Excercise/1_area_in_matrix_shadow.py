def dfs(key, r, c, matrix, visited):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        return
    if visited[r][c] or matrix[r][c] != key:
        return

    visited[r][c] = True
    dfs(key, r - 1, c, matrix, visited)
    dfs(key, r + 1, c, matrix, visited)
    dfs(key, r, c - 1, matrix, visited)
    dfs(key, r, c + 1, matrix, visited)


def solution():
    rows = int(input())
    cols = int(input())
    matrix = [[ch for ch in input()] for _ in range(rows)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    areas = {}
    for r in range(rows):
        for c in range(cols):
            if visited[r][c]:
                continue
            key = matrix[r][c]
            dfs(key, r, c, matrix, visited)
            if key not in areas:
                areas[key] = 0
            areas[key] += 1

    summary = {k: v for k, v in sorted(areas.items(), key=lambda item: item[0])}
    print(f'Areas: {len(areas)}')
    for k, v in summary.items():
        print(f"Letter '{k}' -> {v}")


if __name__ == '__main__':
    solution()