class Edge:
    def __init__(self, source, destination, weight, connected=False):
        self.source = source
        self.destination = destination
        self.weight = weight
        self.connected = connected

    def __str__(self):
        return f'{self.source} - {self.destination}'


def load_inputs():
    args = []
    for _ in range(3):
        args.append(int(input()))
    graph = []
    for _ in range(args[2]):
        line = [ch for ch in input().split(' ')]
        c = True if len(line) == 4 else False
        graph.append(Edge(*[int(x) for x in line[0:3]], c))
    return args[0], args[1], args[2], graph


def solution():
    budget, nodes_num, edges, graph = load_inputs()
    budget_used = 0
    nodes_set = set((n for e in ((el.source, el.destination) for el in graph) for n in e))
    exiting_nodes_set = set((n for e in ((el.source, el.destination) for el in graph if el.connected) for n in e))
    new_nodes_set = nodes_set.difference(exiting_nodes_set)
    max_node_idx = max(list(nodes_set))

    cost = [float('inf')] * (max_node_idx + 1)
    connecting_edges = [None] * (max_node_idx + 1)

    new_nodes = [n for n in new_nodes_set]
    exiting_nodes = [n for n in exiting_nodes_set]
    while nodes_set:
        new_nodes = sorted(new_nodes, key=lambda n: -cost[n])
        exiting_nodes = sorted(exiting_nodes, key=lambda n: -cost[n])
        node = exiting_nodes.pop() if exiting_nodes else new_nodes.pop()
        nodes_set.remove(node)
        edges = [e for e in graph if (e.source == node or e.destination == node) and e not in connecting_edges]
        for edge in edges:
            if edge.destination in exiting_nodes_set and edge.source in exiting_nodes_set and not edge.connected:
                continue
            d = edge.destination if edge.source == node else edge.source
            if d not in nodes_set:
                continue
            if connecting_edges[d] and connecting_edges[d].connected and not edge.connected:
                continue
            if cost[d] > edge.weight:
                cost[d] = edge.weight
                connecting_edges[d] = edge
        if node in new_nodes_set:
            if budget_used + cost[node] > budget:
                break
            budget_used += cost[node]

    print(f'Budget used: {budget_used}')


if __name__ == '__main__':
    solution()
