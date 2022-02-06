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

