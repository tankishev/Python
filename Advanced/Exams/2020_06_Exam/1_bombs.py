# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing.
# If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb materials.
# Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.
# Bombs:
# •	Datura Bombs: 40
# •	Cherry Bombs: 60
# •	Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
# •	On the first line, you will receive the integers representing the bomb effects, separated by ", ".
# •	On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
# •	On the first line, print:
# o	if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
# o	if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
# •	On the second line, print all bomb effects left:
# o	If there are no bomb effects: "Bomb Effects: empty"
# o	If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
# •	On the third line, print all bomb casings left:
# o	If there are no bomb casings: "Bomb Casings: empty"
# o	If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
# •	Then, you need to print all bombs and the count you have of them, ordered alphabetically:
# o	"Cherry Bombs: {count}"
# o	"Datura Bombs: {count}"
# o	"Smoke Decoy Bombs: {count}"


from collections import deque


bombs = {
    'Datura Bombs': {
        'requirement': 40,
        'count': 0}, 
    'Cherry Bombs': {
        'requirement': 60,
        'count': 0},
    'Smoke Decoy Bombs':  {
        'requirement': 120,
        'count': 0}
}

bomb_effect = deque([int(el) for el in input().split(', ')])
bomb_casing = deque([int(el) for el in input().split(', ')])
requirements = [bombs[key]['requirement'] for key in bombs.keys()]
pouch = 0

while bomb_casing and bomb_effect:

    if bomb_casing[-1] + bomb_effect[0] in requirements:
        effect = bomb_effect.popleft()
        casing = bomb_casing.pop()

        for key, value in bombs.items():
            
            if value['requirement'] == effect + casing:
                bombs[key]['count'] += 1
                break
    
    else:
        bomb_casing[-1] -= 5

    pouch = [bombs[key]['count'] for key in bombs.keys() if bombs[key]['count'] >= 3]
    if len(pouch) == 3:
        break

if len(pouch) == 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f'Bomb Effects: ', ', '.join([str(el) for el in bomb_effect]), sep='')
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f'Bomb Casings: ', ', '.join([str(el) for el in bomb_casing]), sep='')
else:
    print("Bomb Casings: empty")

output = [(key, value['count']) for key, value in bombs.items()]
for item in sorted(output):
    print(f'{item[0]}: {item[1]}')
