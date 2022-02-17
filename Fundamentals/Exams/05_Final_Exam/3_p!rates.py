# Until the "Sail" command is given, you will be receiving:
# •	You and your crew have targeted cities, with their population and gold, separated by "||".
# •	If you receive a city that has already been received, you have to increase the population and gold with the given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given. 
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
# o	You have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold. 
# o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# 	You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following message: 
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# Input
# •	On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold and population, separated by "||"
# •	On the following lines, until the "End" command, you will be receiving strings representing the actions described above, separated by "=>"
# Output
# •	After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print all of them, in the following format:
# "Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
# {town2} -> Population: {people} citizens, Gold: {gold} kg
#    …
# {town…n} -> Population: {people} citizens, Gold: {gold} kg"
# •	If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"



targets = {}

while True:
    input_line = input()
    if input_line == 'Sail':
        break
    
    town, pop, gold = input_line.split('||')

    if town in targets:
        targets[town]['pop'] += int(pop)
        targets[town]['gold'] += int(gold)  
    else:
        targets[town] = {'pop': int(pop), 'gold': int(gold)}

while True:
    input_line = input()
    if input_line == 'End':
        break

    tokens = input_line.split('=>')
    command, town = tokens[0], tokens[1]

    if command == 'Plunder':
        people, gold = int(tokens[2]), int(tokens[3])
        
        kills = min(people, targets[town]['pop'])
        gold_plundered = min(gold, targets[town]['gold'])
        
        targets[town]['pop'] -= people
        targets[town]['gold'] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targets[town]['gold'] <= 0 or targets[town]['pop'] <= 0: 
            targets.pop(town)
            print(f"{town} has been wiped off the map!")

    elif command == 'Prosper':
        gold = int(tokens[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            targets[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targets[town]['gold']} gold.")

if len(targets) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

else:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    output = ['{0} -> Population: {1} citizens, Gold: {2} kg'.format(town, stats['pop'], stats['gold']) for town, stats in targets.items()]
    print(*output, sep='\n')

