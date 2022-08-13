from collections import deque

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

rows = len(a) + 1
cols = len(b) + 1
matrix = []
retval = deque()

for _ in range(rows):
    matrix.append([0 for _ in range(cols)])

for r in range(1, rows):
    for c in range(1, cols):
        if a[r - 1] == b[c - 1]:
            val = matrix[r - 1][c - 1] + 1
            matrix[r][c] = val
        else:
            top = matrix[r - 1][c]
            left = matrix[r][c - 1]
            matrix[r][c] = max(top, left)

last_val = matrix[-1][-1]
r = rows - 1
c = cols - 1

while r > 0 and c > 0:
    if a[r - 1] == b[c - 1]:
        retval.appendleft(a[r - 1])
        r -= 1
        c -= 1
    elif matrix[r - 1][c] > matrix[r][c - 1]:
        r -= 1
    else:
        c -= 1

print(*retval, sep=' ')
print(len(retval))