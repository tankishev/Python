# First, you will be given two sequences of integers values on different lines. The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# •	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# •	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# •	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# •	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# •	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.



num_set_1 = set(int(x) for x in input().split())
num_set_2 = set(int(x) for x in input().split())

for _ in range(int(input())):
    tokens = input().split()
    if len(tokens) > 2:
        numbers = list(map(int, tokens[2:]))
    
    if tokens[0] == 'Add' and tokens[1] == 'First':
        num_set_1.update(numbers)
    elif tokens[0] == 'Add' and tokens[1] == 'Second':
        num_set_2.update(numbers)
    elif tokens[0] == 'Remove' and tokens[1] == 'First':
        for x in numbers: num_set_1.discard(x)
    elif tokens[0] == 'Remove' and tokens[1] == 'Second':
        for x in numbers: num_set_2.discard(x)
    elif tokens[0] == 'Check':
        print((num_set_1 >= num_set_2 or num_set_2 >= num_set_1))

print(*sorted(num_set_1), sep=', ')
print(*sorted(num_set_2), sep=', ')