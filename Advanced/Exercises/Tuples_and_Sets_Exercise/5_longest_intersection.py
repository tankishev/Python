# Write a program which finds the longest intersection. You will be given a number N. 
# On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". 
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive. 
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its length in the format: 
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"

intersections = []
max_len = 0
for _ in range(int(input())):
    range_1, range_2 = input().split('-')
    x1, x2 = range_1.split(',')
    y1, y2 = range_2.split(',')
    set_x = set([x for x in range(int(x1), int(x2) + 1)])
    set_y = set([y for y in range(int(y1), int(y2) + 1)])
    intersection = set_x & set_y
    intersections.append((list(intersection), len(intersection)))
    max_len = max(len(intersection), max_len)

output = next(filter(lambda x: x[1] == max_len, intersections))
print(f"Longest intersection is {output[0]} with length {output[1]}")