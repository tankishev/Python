def bubble_sort(l: list):
    n = len(l) - 1
    while n > 0:
        i, j = 0, 1
        is_sorted = True
        while i < n:
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
                is_sorted = False
            i += 1
            j += 1
        if is_sorted:
            break
        n -= 1


a = [int(x) for x in input().split()]
bubble_sort(a)
print(*a, sep=' ')
bubble_sort(a)
print(*a, sep=' ')