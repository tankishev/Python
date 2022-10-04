def dfs(node, graph, visited):
    if node in visited:
        return

    visited.append(node)
    for child in graph[node]:
        dfs(child, graph, visited)


graph = {}
num_nodes = int(input())
num_edges = int(input())
for i in range(1, num_nodes + 1):
    graph[i] = []

for _ in range(num_edges):
    src, dst = [int(x) for x in input().split(' ')]
    graph[src].append(dst)
s_node = int(input())

visited = []
dfs(s_node, graph, visited)
retval = [i for i in range(1, num_nodes + 1) if i not in visited ]
if retval:
    print(*retval, sep=' ')
