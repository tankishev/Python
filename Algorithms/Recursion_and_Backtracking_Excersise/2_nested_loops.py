def gen_states(v, idx=0):
    if idx == len(v):
        print(*v, sep=' ')
        return

    for i in vals:
        v[idx] = i
        gen_states(v, idx + 1)


n = int(input())
vals = list(range(1, n + 1))
a = [1] * n
gen_states(a)
