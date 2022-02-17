# You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
# •	On the first line, print the sum of the negatives
# •	On the second line, print the sum of the positives
# •	On the third line:
# o	If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# o	If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"

def separate_numbers(*args) -> None:
    sum_positive = sum([int(x) for x in args if int(x) > 0])
    sum_negative = sum([int(x) for x in args if int(x) < 0])
    print(sum_negative)
    print(sum_positive)
    if abs(sum_negative) > abs(sum_positive):
        print('The negatives are stronger than the positives')
    if abs(sum_negative) < abs(sum_positive):
        print('The positives are stronger than the negatives')


input_line = input().split()
separate_numbers(*input_line)
