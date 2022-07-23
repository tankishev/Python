def choose_pivot(a: list, lb: int, ub: int) -> int:
    if ub - lb <= 2:
        return ub, a[ub]

    x = (ub - lb + 1) // 2
    vals = {a[idx]: idx for idx in (lb, ub, x)}
    if len(vals.keys()) < 3:
        return ub, a[ub]

    l = list(vals.keys())
    for i in range(2):
        j = i + 1
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
    if l[0] > l[1]:
        return vals[l[0]], l[0]
    return vals[l[1]], l[1]


def quick_sort(a: list, lb_idx: int = 0, ub_idx: int = None) -> list:
    if ub_idx is None:
        ub_idx = len(a) - 1
    if lb_idx >= ub_idx:
        return

    # find good pivot
    p_idx, p = choose_pivot(a, lb_idx, ub_idx)

    # sort algorithm
    if p_idx != ub_idx:
        a[p_idx], a[ub_idx] = a[ub_idx], a[p_idx]
    u_idx = ub_idx - 1
    l_idx = lb_idx
    while True:
        while a[l_idx] <= p and l_idx < ub_idx:
            l_idx += 1
        while a[u_idx] > p and u_idx >= lb_idx:
            u_idx -= 1
        if u_idx < l_idx:
            a[l_idx], a[ub_idx] = a[ub_idx], a[l_idx]
            break
        if a[u_idx] < a[l_idx]:
            a[l_idx], a[u_idx] = a[u_idx], a[l_idx]

    # slit in two and run again
    quick_sort(a, lb_idx, l_idx - 1)
    quick_sort(a, l_idx + 1, ub_idx)


arr = [int(x) for x in input().split()]
quick_sort(arr)
print(*arr, sep=' ')
