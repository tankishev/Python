# You will receive three integer numbers. 
# Write a program that finds if their multiplication (the result) is negative, positive, or zero. 
# Try to do this WITHOUT multiplying the 3 numbers.

num_list = []
for _ in range(3):
    num_list.append(int(input()))

count_negative = len(list(filter(lambda x: x < 0, num_list)))
count_zeroes = len(list(filter(lambda x: x == 0 ,num_list)))

if count_zeroes > 0:
    print('zero')
elif count_negative == 1 or count_negative == 3:
    print('negative')
else:
    print('positive')