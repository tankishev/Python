def insertion_sort(arr: list):
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            for j in range(i):
                if arr[j] > arr[i]:
                    arr.insert(j, arr.pop(i))
                    break
        i += 1
    return arr


a = [int(x) for x in input().split()]
insertion_sort(a)
print(*a, sep=' ')
