# On the first line you will receive the starting quantity of water (integer) in a dispenser. 
# Then, on the next few lines you will be given the names of some people who want to get water (each on separate line)
#  until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
# -	"{liters}" - litters (integer) that the current person in the queue wants to get. 
# Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -	"refill {liters}" - add the given litters in the dispenser.
# At the end print how many litters of water have left in the format: "{left_liters} liters left".

from collections import deque


water = int(input())
queue = deque()
while True:
    name = input()
    if name == 'Start': break
    queue.append(name)

while True:
    command = input()
    if command == 'End': 
        break
    elif command.isnumeric():
        ltr = int(command)
        if water >= ltr:
            print(f"{queue.popleft()} got water")
            water -= ltr
        else:
            print(f"{queue.popleft()} must wait")
    else:
        _, ltr = command.split()
        water += int(ltr)

print(f"{water} liters left")