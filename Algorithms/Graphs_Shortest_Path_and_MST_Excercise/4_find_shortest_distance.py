class Edge:
    def __init__(self, source, destination, weight, directional=False):
        self.source = source
        self.destination = destination
        self.weight = weight

    @property
    def max_id(self):
        return max(self.source, self.destination)


def update(edges, dist, parent):
    updated = False
    for e in edges:
        dist_s = dist[e.source]
        dist_d = dist[e.destination]
        if dist_s != float('inf') and dist_d > dist_s + e.weight:
            dist[e.destination] = dist_s + e.weight
            parent[e.destination] = e.source
            if not updated:
                updated = True
    return updated


def solution():
    # Get inputs
    num_nodes = int(input())
    num_edges = int(input())
    edges = []
    for _ in range(num_edges):
        s, d, w = [int(x) for x in input().split()]
        edges.append(Edge(s, d, w))
    s = int(input())
    d = int(input())

    max_node_id = max([edge.max_id for edge in edges])

    # solve
    dist = [float('inf')] * (max_node_id + 1)
    dist[s] = 0
    parent = [None] * (max_node_id + 1)
    for i in range(num_nodes - 1):
        was_updated = update(edges, dist, parent)
        if not was_updated:
            break

    if i == num_nodes - 2 and update(edges, dist, parent):
        print('Undefined')
    else:
        path = []
        p = d
        while s not in path:
            path.append(p)
            p = parent[p]
        print(*reversed(path), sep=' ')
        print(dist[d])


if __name__ == '__main__':
    solution()
