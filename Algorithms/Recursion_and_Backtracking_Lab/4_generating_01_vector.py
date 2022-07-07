def gen_states(v, idx=0):
    if idx == len(v):
        print(*v, sep='')
        return

    for i in vals:
        v[idx] = i
        gen_states(v, idx + 1)


vals = (0, 1)
a = [vals[0]] * int(input())
gen_states(a)
