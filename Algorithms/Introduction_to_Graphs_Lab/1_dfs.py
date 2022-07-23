def dfs(node: int, graph: dict, component=None, visited=None):
    if visited is None:
        visited = []
    if component is None:
        component = []

    if node in visited:
        return
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child, graph, component, visited)
    if node not in component:
        component.append(node)
    return component


def solve(graph):
    unprocessed = [x for x in graph.keys()]
    components = []
    while unprocessed:
        component = dfs(unprocessed[0], graph)
        components.append(component)
        unprocessed = [x for x in unprocessed if x not in component]

    for component in components:
        retval = ' '.join([str(x) for x in component])
        print(f'Connected component: {retval}')


if __name__ == '__main__':
    nodes = {}
    for n in range(int(input())):
        nodes[n] = [int(x) for x in input().split()]

    solve(nodes)