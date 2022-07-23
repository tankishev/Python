dependencies = {}
graph = {}
retval = []

for _ in range(int(input())):
    k, vals = input().split('->')
    k = k.strip()
    v = vals.strip().split(', ') if vals else []
    graph[k] = v
    if k not in dependencies:
        dependencies[k] = 0
    for el in v:
        if el not in dependencies:
            dependencies[el] = 0
        dependencies[el] += 1

while any(i == 0 for i in dependencies.values()):
    next_nodes = [(k, v) for k, v in dependencies.items() if v == 0]
    for k, v in next_nodes:
        retval.append(k)
        dependencies.pop(k)
        for node in graph[k]:
            dependencies[node] -= 1

if dependencies:
    print('Invalid topological sorting')
else:
    print(f'Topological sorting: {", ".join(str(el) for el in retval)}')
