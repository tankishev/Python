# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
# •	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# •	Columns + rows define the middle letter: 
# o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
# o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
# Input
# •	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
# •	r and c are integers in the range [1, 26]


rows, cols = [int(x) for x in input().split()]

chars = 'abcdefghijklmnopqrstuvwxyz'

for i in range(rows):
    row = [f'{chars[i]}{chars[j]}{chars[i]}' for j in range(i, cols + i)]
    print (*row, sep=' ')