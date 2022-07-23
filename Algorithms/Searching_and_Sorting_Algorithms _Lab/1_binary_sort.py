def binary_search(n: int, a: list, l: int = 0, u: int = None) -> int:
    if u is None:
        u = len(a) - 1

    i = (u + l) // 2
    if a[i] == n:
        return i
    elif l == u:
        return -1
    elif a[i] > n:
        return binary_search(n, a, l, i - 1)
    else:
        return binary_search(n, a, i + 1, u)


arr = [int(x) for x in input().split()]
val = int(input())
print(binary_search(val, arr))
