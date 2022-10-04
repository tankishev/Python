from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, src, dst, rate):
        self.src = src
        self.dst = dst
        self.rate = rate

    def __repr__(self):
        return f'Edge({self.src}, {self.dst}, {self.rate})'


class Graph:
    def __init__(self):
        self.__nodes = set()
        self.edges = []

    @property
    def nodes(self):
        return list(self.__nodes)

    def node_children(self, node):
        return [(edge.dst, edge.rate) for edge in self.edges if edge.src == node]

    def node_parents(self, node):
        return [(edge.src, edge.rate) for edge in self.edges if edge.dst == node]

    def add_edges(self, line):
        src, dst, rate = line.split(' ')
        self.edges.append(Edge(src, dst, float(rate)))
        self.__nodes.update((src, dst))


def get_inputs():
    graph = Graph()
    for _ in range(int(input())):
        graph.add_edges(input())
    ccy = input()
    return graph, ccy


def get_best_rates(node, graph, parents, rates):
    unvisited = set(graph.nodes)
    pq = PriorityQueue()
    pq.put((-1, node))

    while pq.queue:
        ccy_rate, ccy = pq.get()
        ccy_rate *= -1
        if ccy not in unvisited:
            continue

        for pair_ccy, fx_rate in graph.node_children(ccy):
            if pair_ccy in unvisited:
                recorded_rate = rates[pair_ccy]
                this_rate = ccy_rate * fx_rate
                if this_rate > recorded_rate:
                    rates[pair_ccy] = this_rate
                    parents[pair_ccy] = ccy
                    pq.put((-rates[pair_ccy], pair_ccy))
        unvisited.remove(ccy)


def print_route(node, target, parents):
    route = deque()
    route.appendleft(target)
    route.appendleft(node)
    parent = parents[node]

    while parent != target:
        route.appendleft(parent)
        parent = parents[parent]

    route.appendleft(target)
    print(*route, sep=' ')


def solution():
    graph, ccy = get_inputs()
    parents = dict((node, None) for node in graph.nodes)
    best_rate = dict((node, -9e6) for node in graph.nodes)
    parents[ccy] = ccy
    best_rate[ccy] = 1
    get_best_rates(ccy, graph, parents, best_rate)
    ccy_exchanges = [(ccy_pair, best_rate[ccy_pair] * fx_rate) for ccy_pair, fx_rate in graph.node_parents(ccy)]
    arbitrages = [el for el in ccy_exchanges if el[1] > 1]

    # print(best_rate)
    # print(arbitrages)

    if arbitrages:
        arb_ccy, rate = sorted(arbitrages, key=lambda el: -el[1])[0]
        print('True')
        print_route(arb_ccy, ccy, parents)
    else:
        print('False')
        print(*[f'{fx}: {rate:.3f}' for fx, rate in best_rate.items()], sep='\n')


if __name__ == '__main__':
    solution()
