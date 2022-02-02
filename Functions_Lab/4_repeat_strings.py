# Write a function that receives a string and a counter n. The function should return a new string – the result of repeating the old string n times. Print the result of the function. Try using lambda.

input_str = input()
n = int(input())
output = lambda x: input_str * x

print (output(n))