# Tony and Andi love playing in the snow and having snowball fights, but they always argue about which makes the best snowballs. 
# They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.

# You will receive N – an integer, the number of snowballs being made by Tony and Andi.

# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).

# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
# •	On the first input line, you will receive N – the number of snowballs.
# •	On the next N*3 input lines, you will be receiving data about each snowball. 
# Output
# •	You need to print the highest calculated snowball's value in the format: 
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints
# •	The number of snowballs (N) will be an integer in range [0, 100].
# •	The weight is an integer in the range [0, 1000].
# •	The time is an integer in the range [1, 500].
# •	The quality is an integer in the range [0, 100].

N = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_value = 0

for _ in range(N):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_weight / snowball_time) ** snowball_quality

    if value > best_value:
        best_value = value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality

print(f"{best_weight} : {best_time} = {best_value:.0f} ({best_quality})")