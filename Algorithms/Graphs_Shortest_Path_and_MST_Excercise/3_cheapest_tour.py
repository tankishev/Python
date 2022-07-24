class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f'{self.source} - {self.destination}'


def load_inputs():
    graph = []
    towns = int(input())
    streets = int(input())
    for _ in range(streets):
        s, d, w = [int(x) for x in input().split(' - ')]
        graph.append(Edge(s, d, w))
    return graph


def solution():
    graph = load_inputs()
    nodes = list(set((n for e in ((el.source, el.destination) for el in graph) for n in e)))
    threes = [set([n]) for n in nodes]
    forest = []

    for edge in sorted(graph, key=lambda e: e.weight):
        s, d = edge.source, edge.destination
        s_three = next(el for el in threes if s in el)
        d_three = next(el for el in threes if d in el)
        if s_three == d_three:
            continue
        forest.append(edge)
        s_three.update(d_three)
        threes.remove(d_three)

    print(f'Total cost: {sum([e.weight for e in forest])}')


if __name__ == '__main__':
    solution()