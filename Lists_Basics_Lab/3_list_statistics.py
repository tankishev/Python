# On the first line, you will receive a number n. 
# On the following n lines, you will receive integers. 

# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message: 
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

n = int(input())
lst_input = []
for _ in range(n):
    lst_input.append(int(input()))

lst_positive = list(filter(lambda x: x >= 0, lst_input))
lst_negative = list(filter(lambda x: x < 0, lst_input))

count_of_positives = len(lst_positive)
sum_of_negatives = sum(lst_negative)

print(lst_positive)
print(lst_negative)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
