# Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on your first day at work.
# You will receive a single line containing some food (keys) and quantities (values). 
# They will be separated by a single space (the first element is the key, the second – the value, and so on). 
# Create a dictionary with all the keys and values and print it on the console.

input_data = input().split(' ')
keys = [x for i, x in enumerate(input_data) if i % 2 == 0]
values = [int(x) for i, x in enumerate(input_data) if i % 2 != 0]

result = {}

for key, value in zip(keys, values):
	result[key] = value
print(result)