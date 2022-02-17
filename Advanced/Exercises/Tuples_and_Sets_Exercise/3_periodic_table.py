# Write a program that keeps all the unique chemical elements. 
# On the first line you will be given a number n - the count of input lines that you are going to receive. 
# On the next n lines, you will be receiving chemical compounds, separated by a single space. 
# Your task is to print all the unique ones on separate lines (the order does not matter):

elem = set()
for _ in range(int(input())):
    elem.update(input().split())

print(*elem, sep='\n')