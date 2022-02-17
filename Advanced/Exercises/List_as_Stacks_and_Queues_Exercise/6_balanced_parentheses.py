# You will be given a sequence consisting of parentheses. 
# Your job is to determine whether the expression is balanced. 
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding 
# closing parenthesis that occurs after the former. There will be no interval symbols between the parentheses. 
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.

my_stack = []
balanced = True
bundle = {'(':')','{':'}','[':']'}
input_line = input()

for x in input_line:
    if x in bundle.keys():
        my_stack.append(x)
    elif my_stack and x == bundle.get(my_stack.pop()):
        continue
    else:
        balanced = False
        break

if balanced:
    print('YES')
else:
    print('NO')
