from queue import PriorityQueue


def bfs(node: int, target: int, graph: dict, unvisited: set, distances: list, parents: list):
    pq = PriorityQueue()
    pq.put((0, node))
    while pq.queue:
        traveled_distance, node = pq.get()
        if node == target:
            unvisited.remove(node)
            break
        if node not in unvisited:
            continue
        for child, distance in graph[node].items():
            if child in unvisited:
                recorded_distance = distances[child]
                if traveled_distance + distance < recorded_distance:
                    distances[child] = traveled_distance + distance
                    parents[child] = node
                    pq.put((distances[child], child))
        unvisited.remove(node)


def solution():
    unvisited = set()
    num_edges = int(input())
    edges = []
    for _ in range(num_edges):
        node = [int(x) for x in input().split(', ')]
        edges.append(node)
        unvisited.add(node[0])
        unvisited.add(node[1])

    graph = {el: {} for el in list(unvisited)}
    for edge in edges:
        a, b, d = edge
        graph[a][b] = d
        graph[b][a] = d

    start = int(input())
    end = int(input())

    distances = [9e6] * (max(unvisited) + 1)
    distances[0] = 0
    parents = [None] * len(distances)
    bfs(start, end, graph, unvisited, distances, parents)

    if end in unvisited:
        print('There is no such path.')
    else:
        print(distances[end])
        path = [end]
        parent = parents[end]
        while parent is not None:
            path.append(parent)
            parent = parents[parent]
        print(*reversed(path), sep=" ")


if __name__ == '__main__':
    solution()
