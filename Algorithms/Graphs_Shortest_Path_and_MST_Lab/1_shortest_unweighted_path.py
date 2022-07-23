from collections import deque


def bfs(start, end, graph):
    visited = []
    children = {}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visited.append(node)
        for child in graph[node]:
            if child not in visited and child not in queue:
                queue.append(child)
                children[child] = node
        if end in visited:
            break
    return children


def solution():
    num_nodes = int(input())
    num_edges = int(input())
    graph = {i: [] for i in range(1, num_edges + 1)}
    edges = []

    for _ in range(num_edges):
        edge = [int(el) for el in input().split()]
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    start = int(input())
    end = int(input())

    children = bfs(start, end, graph)
    child = end
    output = [end]
    while child != start:
        child = children[child]
        output.append(child)
    print(f'Shortest path length is: {len(output)-1}')
    print(*reversed(output), sep=' ')


if __name__ == '__main__':
    solution()
