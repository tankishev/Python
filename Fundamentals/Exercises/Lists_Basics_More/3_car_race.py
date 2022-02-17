# Write a program that announces the winner of a car race. 
# You will receive a sequence of numbers. Each number represents the time needed for the car to pass through that step (the index). 
# There will be two cars. The first one starts from the left side, and the other one starts from the right side. The middle index of the sequence is the finish line. 
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time). 
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

input_data = input()
input_list = [int(x) for x in input_data.split(' ')]
left_list = input_list[:(len(input_list) // 2)]
input_list.reverse()
right_list = input_list[:(len(input_list) // 2)]

left_time = 0
right_time = 0

i = 0

while i < len(left_list):
    if left_list[i] == 0:
        left_time *= 0.8
    else: 
        left_time += left_list[i]

    if right_list[i] == 0:
        right_time *= 0.8
    else: 
        right_time += right_list[i]

    i += 1

else:
    if left_time < right_time:
        print(f"The winner is left with total time: {left_time:.1f}")
    elif  left_time > right_time:
        print(f"The winner is right with total time: {right_time:.1f}")