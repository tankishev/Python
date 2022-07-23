def bfs(node, graph, visited=None, component=None):
    if visited is None:
        visited = set()
    if component is None:
        component = []

    if node in visited or node not in graph.keys():
        return
    visited.add(node)

    if node not in component:
        component.append(node)

    for child in graph[node]:
        if child not in component:
            component.append(child)

    for child in graph[node]:
        bfs(child, graph, visited, component)

    return component


nodes = {
    7: [19, 21, 14],
    19: [1, 12, 31],
    21: [31, 23],
    14: [23, 6],
}

print(bfs(7, nodes))
