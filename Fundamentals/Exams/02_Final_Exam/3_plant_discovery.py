# You have now returned from your world tour. On your way, you have discovered some new plants, 
# and you want to gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines, you will be given some information about the 
# plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it later. 
# If you receive a plant more than once, update its rarity.

# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"

# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The plants should be sorted by rarity in descending order. 
# If two or more plants have the same rarity value sort them by average rating in descending order. 
# The average rating should be formatted to the second decimal place.

# Input / Constraints
# •	You will receive the input as described above
# •	JavaScript: you will receive a list of strings

# Output
# •	Print the information about all plants as described above


plants = {}
output = []

def avg(list: list) -> float:
    if len(list) == 0:
        return 0
    else:
        return sum(list) / len(list)

for _ in range(int(input())):
    plant, rarity = input().split('<->')
    plants[plant] = {'rarity':int(rarity), 'ratings':[]}

while True:
    input_line = input()
    if input_line == 'Exhibition':
        break

    tokens = input_line.split(' - ')
    command, plant = tokens[0].split(': ')
    
    if plant in plants:

        if command == 'Rate':
            rating = int(tokens[1])
            plants[plant]['ratings'].append(rating)

        elif command == 'Update':
            new_rarity = int(tokens[1])
            plants[plant]['rarity'] = new_rarity

        elif command == "Reset":
            plants[plant]['ratings'].clear()
    
    else:
        print('error')


s = sorted(plants.items(), 
    key= lambda item: 
        (item[1]['rarity']
        ,avg(item[1]['ratings']))
        ,reverse=True)

print('Plants for the exhibition:')
for p in s:
    name = p[0]
    rarity = p[1]['rarity']
    average_rating = avg(p[1]['ratings'])

    print(f'- {name}; Rarity: {rarity}; Rating: {average_rating:.2f}')

