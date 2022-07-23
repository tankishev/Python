from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight, directional=False):
        self.source = source
        self.destination = destination
        self.weight = weight


def solution():
    # get inputs
    num_nodes = int(input())
    num_edges = int(input())
    edges = []
    for _ in range(num_edges):
        s, d, w = [int(x) for x in input().split(' ')]
        edges.append(Edge(s, d, w / 100))
    start = int(input())
    end = int(input())

    unvisited = set((n for e in ((el.source, el.destination) for el in edges) for n in e))
    reliability = [0] * (max(list(unvisited)) + 1)
    reliability[start] = 1
    parent = [None] * len(reliability)
    parent[start] = start

    pq = PriorityQueue()
    pq.put((-1, start))
    while pq.queue:
        path_quality, source = pq.get()
        path_quality *= -1
        if source not in unvisited:
            continue
        if source == end:
            unvisited.remove(source)
            break
        roads = [e for e in edges if source in (e.source, e.destination)]
        connected_towns = [(c, e.weight) for e in roads for c in (e.destination, e.source) if c != source]
        for town, town_road_quality in connected_towns:
            if town in unvisited:
                recorded_road_quality = reliability[town]
                if path_quality * town_road_quality > recorded_road_quality:
                    reliability[town] = path_quality * town_road_quality
                    parent[town] = source
                    pq.put((-reliability[town], town))
        unvisited.remove(source)

    print(f'Most reliable path reliability: {reliability[end] * 100:.2f}%')
    path = [end]
    p = parent[end]
    while start not in path:
        path.append(p)
        p = parent[p]
    print(*reversed(path), sep=' -> ')


if __name__ == '__main__':
    solution()
