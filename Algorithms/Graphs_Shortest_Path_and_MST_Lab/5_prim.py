class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f'{self.source} - {self.destination}'


def load_inputs():
    graph = []
    for _ in range(int(input())):
        s, d, w = [int(x) for x in input().split(', ')]
        graph.append(Edge(s, d, w))
    return graph


def solution():
    graph = load_inputs()
    if not graph:
        exit()
    nodes = set((n for e in ((el.source, el.destination) for el in graph) for n in e))
    cost = [float('inf')] * (max(list(nodes)) + 1)
    connecting_edges = [None] * (max(list(nodes)) + 1)

    while nodes:
        node, c = next(iter(sorted([(n, c) for n, c in enumerate(cost) if n in nodes], key=lambda el: el[1])))
        nodes.remove(node)
        edges = [e for e in graph if e.source == node or e.destination == node]
        for edge in edges:
            d = edge.destination if edge.source == node else edge.source
            if d in nodes and cost[d] > edge.weight:
                cost[d] = edge.weight
                connecting_edges[d] = edge

    forest = [el for el in connecting_edges if el]
    print(*forest, sep='\n')


if __name__ == '__main__':
    solution()
