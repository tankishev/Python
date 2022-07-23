def dfs(node, graph, visited=None):
    if visited is None:
        visited = []
    if node in visited:
        return
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child, graph, visited)
    return visited


def gen_graph(edges: list) -> dict:
    graph = {}
    for edge in edges:
        nodes = [int(node) for node in edge.split(' - ')]
        a, b = nodes
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)
    return graph


def print_format(line):
    a, b = line.split(' - ')
    return f'{min(a,b)} {max(a,b)}'


def solution():
    num_buildings = int(input())
    roads = []
    for _ in range(int(input())):
        roads.append(input())

    important_roads = []
    for idx in range(len(roads)):
        temp_graph = gen_graph([el for i, el in enumerate(roads) if i != idx])
        buildings = dfs(next(iter(temp_graph.keys())), temp_graph)
        if len(buildings) != num_buildings:
            important_roads.append(roads[idx])

    if important_roads:
        print('Important streets:')
        print(*[print_format(el) for el in sorted(important_roads)], sep='\n')


if __name__ == '__main__':
    solution()
