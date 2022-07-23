from collections import deque


def bfs(start, end, graph, path):
    queue = deque([start])
    visited = []
    while queue:
        node = queue.popleft()
        if node == end:
            break
        visited.append(node)
        for child in graph[node]:
            if child not in visited and child not in queue:
                queue.append(child)
                path[child] = node


def solution():
    # get inputs
    num_edges = int(input())
    num_pairs = int(input())
    graph = {}
    for _ in range(num_edges):
        nodes = [el for el in input().split(':')]
        s = int(nodes[0])
        if s not in graph:
            graph[s] = []
        if len(nodes) > 1:
            destinations = [int(x) for x in nodes[1].split()]
            if destinations:
                graph[s].extend(destinations)

    pairs = []
    for _ in range(num_pairs):
        pairs.append([int(x) for x in input().split('-')])

    max_node_id = max(list(graph.keys()))
    for pair in pairs:
        s, d = pair
        path = [0] * (max_node_id + 1)
        bfs(s, d, graph, path)

        dist = 0
        p = d
        if path[d] == 0:
            dist = -1
        else:
            while path[p] != 0:
                dist += 1
                p = path[p]

        print(f'{{{s}, {d}}} -> {dist}')


if __name__ == '__main__':
    solution()
