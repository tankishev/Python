char = '*'
num = int(input())
for i in range(num):
    print(char*(i+1))
for i in reversed(range(num-1)):
    print(char*(i+1))