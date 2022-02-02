# Write a program that reads four integer numbers. 
# It should add the first to the second number, integer divide the sum by the third number, 
# and multiply the result by the fourth number. Print the final result.

i1 = int(input())
i2 = int(input())
i3 = int(input())
i4 = int(input())

result = i1 + i2
result = result // i3
result *= i4

print (result)