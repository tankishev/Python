# Write a program that receives a single string (integers separated by a comma and space ", "), 
# finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting integer list.

input_data = input()
num_list = [int(x) for x in input_data.split(', ')]
numbers = len(num_list)
i = 0
print_list = []

while i < numbers:
    if num_list[i] != 0:
        print_list.append(num_list.pop(i))
        numbers -= 1
        continue
    i += 1

print_list.extend(num_list)

print (print_list)