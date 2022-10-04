def gen_paths(rows, cols, r=0, c=0, paths_found=None):
    if paths_found is None:
        paths_found = [0]

    if r == rows or c == cols:
        return

    if (r, c) == (rows - 1, cols - 1):
        paths_found[0] += 1
        return

    gen_paths(rows, cols, r + 1, c, paths_found)
    gen_paths(rows, cols, r, c + 1, paths_found)

    return paths_found[0]


m = int(input())
n = int(input())
print(gen_paths(m, n))
