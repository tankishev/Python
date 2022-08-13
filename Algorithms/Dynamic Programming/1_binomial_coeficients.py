def factorial(n, f_mem=None):
    if f_mem is None:
        f_mem = {}
    if n == 0:
        return 1
    if n in f_mem.keys():
        return f_mem[n]
    else:
        val = n * factorial(n-1, f_mem)
        f_mem[n] = val
        return val


def func(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


n = int(input())
k = int(input())
print(int(func(n, k)))


