# You will be given a number. Print the largest number that can be formed from the digits of the given number.

n = input()
digits  = [int(x) for x in n]
digits.sort(reverse=True)
result = ''
for d in digits:
    result += str(d)
print(result)

