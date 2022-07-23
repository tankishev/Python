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


def is_acyclic(graph: dict) -> bool:
    temp_graph = {k: [el for el in v] for k, v in graph.items()}
    while any(len(v) == 1 for v in temp_graph.values()):
        k, v = next((k, v[0]) for k, v in temp_graph.items() if len(v) == 1)
        temp_graph.pop(k)
        if len(temp_graph[v]) == 1:
            temp_graph.pop(v)
        else:
            temp_graph[v].remove(k)
    return len(temp_graph) == 0


def get_components(graph: dict) -> list:
    unprocessed = [el for el in graph.keys()]
    components = []
    while unprocessed:
        component = dfs(unprocessed[0], graph)
        components.append(component)
        unprocessed = [el for el in unprocessed if el not in component]
    return components


def solution():
    graph = {}
    for _ in range(int(input())):
        n, vs = input().split('->')
        n = n.strip()
        v = [el for el in vs.strip().split()] if vs else []
        graph[n] = v

    components = [sorted(component) for component in get_components(graph)]

    removed = []
    for component in sorted(components, key=lambda el: el[0]):
        sub_graph = {k: sorted(graph[k], reverse=True) for k in sorted(component)}
        acyclic = is_acyclic(sub_graph)
        while not acyclic:
            for k, v in sub_graph.items():
                while len(v) > 1 and len(sub_graph[v[-1]]) > 1 and not acyclic:
                    n = v.pop()
                    sub_graph[n].remove(k)
                    removed.append(f'{k} - {n}')
                    acyclic = is_acyclic(sub_graph)

    print(f'Edges to remove: {len(removed)}')
    print(*sorted(removed), sep='\n')


if __name__ == '__main__':
    solution()
