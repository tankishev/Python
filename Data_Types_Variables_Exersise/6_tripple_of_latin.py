# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

N = int(input())

a_index = ord('a')

for i in range(N):
    for j in range(N):
        for k in range(N):
            print(chr(a_index+i) + chr(a_index+j) + chr(a_index+k))


