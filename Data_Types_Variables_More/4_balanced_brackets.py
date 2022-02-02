# On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
# •	Opening bracket – "(",
# •	Closing bracket – ")" or
# •	Random string
# Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced. You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.


n = int(input())

open_bracket = False

for _ in range(n):
    input_str = input()
    if input_str == ')' and not open_bracket:
        open_bracket = True
        break
    if input_str == '(':
        if open_bracket:
            break
        else:
            open_bracket = True

    if open_bracket and ')' in  input_str:
        open_bracket = False

if open_bracket:
    print('UNBALANCED')
else:
    print('BALANCED')


