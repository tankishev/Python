res = False
for _ in range(3):
    a = int(input())
    if res == False:
        res = a
    if a > res:
        res = a
print(res)