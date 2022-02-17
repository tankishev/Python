# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".


primary = []
secondary = []

for i in range(int(input())):
    row = [int(x) for x in input().split(', ')]
    primary.append(row[i])
    secondary.append(row[-1-i])

print(f"Primary diagonal: ", ', '.join([str(x) for x in primary]), f'. Sum: {sum(primary)}', sep='')
print(f"Secondary diagonal: ", ', '.join([str(x) for x in secondary]), f'. Sum: {sum(secondary)}', sep='')