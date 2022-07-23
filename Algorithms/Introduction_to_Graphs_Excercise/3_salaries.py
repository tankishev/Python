def dfs(node, graph, visited=None, salaries=None) -> int:
    if visited is None:
        visited = []
    if salaries is None:
        salaries = {}
    if node in visited:
        return salaries[node]

    visited.append(node)
    salary = 0
    if not graph[node]:
        salary += 1
    else:
        for child in graph[node]:
            salary += dfs(child, graph, visited, salaries)

    salaries[node] = salary
    return salary


def solution():
    n = int(input())
    graph = {k: [] for k in range(n)}
    for i in range(n):
        line = input()
        graph[i] = [j for j in range(n) if line[j] == 'Y']

    total_salaries = 0
    for i in range(n):
        total_salaries += dfs(i, graph)
    print(total_salaries)


if __name__ == '__main__':
    solution()


