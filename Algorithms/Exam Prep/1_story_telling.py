dependencies = {}
graph = {}
retval = []

while True:
    line = input()
    if line == 'End':
        break

    k, vals = line.split('->')
    k = k.strip()
    v = vals.strip().split(' ') if vals else []
    graph[k] = v

    if k not in dependencies:
        dependencies[k] = 0

    for el in v:
        if el not in dependencies:
            dependencies[el] = 0
        dependencies[el] += 1

while any(i == 0 for i in dependencies.values()):
    k, v = [(k, v) for k, v in dependencies.items() if v == 0][-1]
    retval.append(k)
    dependencies.pop(k)
    for node in graph[k]:
        dependencies[node] -= 1

print(f'{" ".join(str(el) for el in retval)}')
