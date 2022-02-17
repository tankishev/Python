# You are driving a truck on a circle road with N petrol pumps on it. The petrol pumps are numbered 0 to (N−1) (both inclusive). 
# For each petrol pump you will receive two pieces of information (separated by a single space): 
# -	the amount of petrol that petrol pump will give
# -	the distance from that petrol pump to the next petrol pump (kilometers)
# Initially, you have a tank of infinite capacity carrying no petrol. 
# The truck can start the tour at any of the petrol pumps and it will move one kilometer for each liter of the petrol. 
# Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. 
# Input
# •	On the first line you will receive the number of petrol pumps - N
# •	On the next N-lines you will receive the amount of petrol that petrol pump will give and 
# the distance between that petrol pump and the next petrol pump, separated by single space
# Output
# •	An integer which will be the smallest index of a petrol pump from which you can start the tour
# Constraints
# •	1 ≤ N ≤ 1000001
# •	1 ≤ Amount of petrol, Distance ≤ 1000000000
# •	You will always have at least one point from where the truck will be able to complete the circle


from collections import deque


def try_circle(pumps_data, starting_pump) -> bool:
    fuel = 0
    for i in range(len(pumps_data)):
        ltr, km = pumps_data[i]
        fuel += ltr - km
        if fuel < 0:
            return False
    return True

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    data = tuple(map(int, input().split()))
    pumps.append(data)

for i in range(len(pumps)):
    if try_circle(tuple(pumps), i):
        break
    pumps.rotate(-1)
print(i)

