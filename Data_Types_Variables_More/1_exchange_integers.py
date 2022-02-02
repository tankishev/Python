# Read two integer numbers and, after that, exchange their values. Print the variable values before and after the exchange, as shown below:

a = int(input())
b = int(input())

print(f'Before:\na = {a}\nb = {b}')

a, b = b, a

print(f'After:\na = {a}\nb = {b}')




