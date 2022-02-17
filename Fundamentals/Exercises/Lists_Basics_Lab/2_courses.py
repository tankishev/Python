# On the first line, you will receive a single number n. 
# On the following n lines, you will receive names of courses. 
# You should create a list of courses and print it.

N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

print(lst)

