# Input
# •	Read from the console a single line holding space-separated integers.
# Output
# •	Print the above-described numbers on a single line, space-separated. 
# •	If less than 5 numbers hold the property mentioned above, print less than 5 numbers. 
# •	Print "No" if no numbers hold the above property.
# Constraints
# •	All input numbers are integers in the range [-1 000 000 … 1 000 000]. 
# •	The count of numbers is in the range [1…10 000].

lst = [int(x) for x in input().split(' ')]
average = sum(lst) / len(lst)
lst.sort(reverse=True)

result = ''
for i in range(len(lst)):
    if lst[i] > average:
        result += str(lst[i]) + ' '
    else:
        break
    if i == 4:
        break

if result == '':
    result = 'No'
    
print(result)