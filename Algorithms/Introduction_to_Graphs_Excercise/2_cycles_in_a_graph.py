dependencies = {}
while True:
    data = input()
    if data == 'End':
        break
    k, v = data.split('-')
    if k not in dependencies:
        dependencies[k] = 0
    if v not in dependencies:
        dependencies[v] = 0
    dependencies[v] += 1

print(f'Acyclic: {("No", "Yes")[any(v == 0 for v in dependencies.values())]}')
