from collections import deque

class Edge:
    def __init__(self, src, dest, distance):
        self.src = src
        self.dest = dest
        self.distance = distance

    @property
    def nodes(self):
        return self.src, self.dest


class Graph:
    def __init__(self, nodes: set):
        self.edges = []
        self.nodes = nodes

    def add_edges(self, line):
        a, b, d = [int(x) for x in line.split(' ')]
        self.edges.append(Edge(a, b, d))
        self.nodes.update((a, b))

    def extend(self, other):
        self.nodes = self.nodes.union(other.nodes)
        self.edges.extend(other.edges)


def get_input():
    n = int(input())
    m = int(input())
    l = int(input())

    nodes = set(i for i in range(n))
    graph = Graph(nodes)
    for _ in range(m):
        graph.add_edges(input())

    strikes = []
    for _ in range(l):
        node, strike = [int(x) for x in input().split(' ')]
        strikes.append((node, strike))

    return n, graph, strikes


def gen_forest(graph):
    forest = [Graph(set([n])) for n in list(graph.nodes)]

    sorted_edges = sorted(graph.edges, key=lambda el: -el.distance)
    while sorted_edges:
        edge = sorted_edges.pop()
        s, d = edge.nodes
        s_tree = next(el for el in forest if s in el.nodes)
        d_tree = next(el for el in forest if d in el.nodes)

        if s_tree != d_tree:
            s_tree.edges.append(edge)
            s_tree.extend(d_tree)
            forest.remove(d_tree)

    return forest


def record_damage(node, tree, hit, damage):
    queue = deque()
    queue.append(node)
    next_queue = []
    processed = []

    while queue:
        target = queue.popleft()
        damage[target] += hit
        processed.append(target)
        for edge in tree.edges:
            if target in edge.nodes:
                next_target = [n for n in edge.nodes if n != target][0]
                if next_target not in next_queue and next_target not in processed:
                    next_queue.append(next_target)
        if not queue and next_queue:
            queue.extend(next_queue)
            next_queue.clear()
            hit = hit // 2


def main():
    nodes, graph, strikes = get_input()
    damage = [0] * nodes
    forest = gen_forest(graph)
    for n, d in strikes:
        tree = next(el for el in forest if n in el.nodes)
        record_damage(n, tree, d, damage)
    print(max(damage))


if __name__ == '__main__':
    main()
