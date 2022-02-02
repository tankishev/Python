# Write a program, which sums the ASCII codes of N characters and prints the sum on the console. 
# On the first line, you will receive N – the number of lines. 
# On the following N lines – you will receive a letter per line. Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].

n = int(input())
ascii_sum =  0

for _ in range(n):
    char = input()
    ascii_sum += ord(char)

print(f"The sum equals: {ascii_sum}")


