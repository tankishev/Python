# As a young baker, you are baking the bread out of the bakery. 
# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# 
# •	If the event is "rest":
# o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You gained {gained_energy} energy.". 
# o	After that, print your current energy: "Current energy: {current_energy}.".
# 
# •	If the event is "order": 
# o	You've earned some coins (the number in the second part). 
# o	Each time you get an order, your energy decreases by 30 points.
# 	If you have the energy to complete the order, print: "You earned {earned} coins.".
# 	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# 
# •	In any other case, you have an ingredient you should buy. The second part of the event contains the coins you should spend. 
# o	If you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over. 

# If you managed to handle all events through the day, print on the following 3 lines: 
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"

# Input / Constraints
# You will receive a string representing the working day events, separated with '|' (vertical bar) in the format:
# "event1|event2| … eventN".
# Each event contains an event name or an ingredient and a number, separated by a dash in the format: "{event/ingredient}-{number}"
# Output
# Print the corresponding messages described above.

energy = 100
coins = 100
success = True
events_handled = 0

input_str = input()
if len(input_str) > 0:
    event_data = input_str.split('|')
    event_data = [event.split('-') for event in event_data]
    for event in event_data:
        number = int(event[1])
        if event[0] == 'rest':
            gained_energy = min(number, 100 - energy)
            energy += gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        
        elif event[0] == 'order':
            if energy >= 30:
                energy -= 30
                coins += number
                print(f"You earned {number} coins.")
            else:
                energy += 50
                print("You had to rest!")
        
        else:
            ingredient = event[0]
            if coins >= number:
                print(f"You bought {ingredient}.")
                coins -= number
            else:
                success = False
                print(f"Closed! Cannot afford {ingredient}.")
                break

    if success:
        print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")