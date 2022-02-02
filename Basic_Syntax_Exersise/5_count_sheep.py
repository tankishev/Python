# If you can't fall asleep, try counting sheep! You will be given a positive integer, 3, for example. You should return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e., integers greater than 0.
# Examples
# Input	Output
# 5	1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...
# 1	1 sheep...

sheep = ' sheep...'
n = int(input())
res = ''
for i in range(n):
    res += str(i+1)
    res += sheep
print(res)