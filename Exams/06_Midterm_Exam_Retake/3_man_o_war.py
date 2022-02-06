# Create a program that tracks the battle and either chooses a winner or prints a stalemate. 
# On the first line, you will receive the status of the pirate ship, which is a string representing integer sections separated by ">". 
# On the second line, you will receive the same type of status, but for the warship: 
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach. 
# The following lines represent commands until "Retire":
# •	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and if not, skip the command. 
#    If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."
# •	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
# "You lost! The pirate ship has sunken."
# •	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.
# •	"Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity. Print the following:
# "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"
# Input
# •	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# •	On the 2nd line, you are going to receive the status of the warship
# •	On the 3rd line, you will receive the maximum health a section of a ship can reach.
# •	On the following lines, until "Retire", you will be receiving commands.
# Output
# •	Print the output in the format described above.

pirate_stats = list(map(int,input().split('>')))
ws_stats = list(map(int,input().split('>')))
section_cap = int(input())
stalemate = True

while True:
    input_line = input()
    if input_line == 'Retire':
        break

    tokens = input_line.split(' ')
    command = tokens[0]

    if command == 'Fire':
        section = int(tokens[1])
        damage = int(tokens[2])
        
        if 0 <= section < len(ws_stats):
            ws_stats[section] -= damage
            if ws_stats[section] <= 0:
                print('You won! The enemy ship has sunken.')
                stalemate = False
                break
             
    elif command == 'Defend':
        i1 = int(tokens[1]) 
        i2 = int(tokens[2])
        damage = int(tokens[3])

        if min(i1,i2) >= 0 and max(i1,i2) < len(pirate_stats):
            pirate_stats = [x - damage if i1 <= i <= i2 else x for i, x in enumerate(pirate_stats)]
            if min(pirate_stats) <= 0:
                print("You lost! The pirate ship has sunken.")
                stalemate = False
                break

    elif command == 'Repair':
        i = int(tokens[1])
        repair = int(tokens[2])

        if 0 <= i < len(pirate_stats):
            pirate_stats[i] = min(pirate_stats[i] + repair, section_cap)

    elif command == 'Status':
        need_repair = [x for x in pirate_stats if x < section_cap*0.2]
        print(f"{len(need_repair)} sections need repair.")


if stalemate:
    print(f"Pirate ship status: {sum(pirate_stats):.0f}")
    print(f"Warship status: {sum(ws_stats):.0f}")
