def merge(a: list, b: list) -> list:
    c = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] <= b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    while a_idx < len(a):
        c.append(a[a_idx])
        a_idx += 1
    while b_idx < len(b):
        c.append(b[b_idx])
        b_idx += 1
    return c


def merge_sort(l: list) -> list:
    if len(l) == 1:
        return l
    idx = (len(l) + 1) // 2
    a = merge_sort(l[0: idx])
    b = merge_sort(l[idx:])
    return merge(a, b)


arr = [int(x) for x in input().split()]
sorted_arr = merge_sort(arr)
print(*sorted_arr, sep=' ')
