# Heroes III is the best game ever. Everyone loves it and everyone plays it all the time. Simon is no exclusion to this rule. 
# His favorite units in the game are all types of dragons – black, red, gold, azure etc. 
# He likes them so much that he gives them names and keeps logs of their stats: damage, health, and armor. 
# The process of aggregating all the data is quite tedious, so he would like to have a program doing it. 
# Since he is no programmer, it's your task to help him.
# 
# You need to categorize dragons by their type. For each dragon, identified by name, 
# keep information about his stats (damage, health, and armor). 
# Type is preserved as in the order of input, but dragons are sorted alphabetically by their name. 
# For each type, you should also print the average damage, health, and armor of the dragons. For each dragon, print his own stats. 
# There may be missing stats in the input, though. If a stat is missing you should assign it default values. 
# Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}". 
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. 
# Any of the integers may be assigned "null" value. See the examples below for better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones. 
# Two dragons are considered equal if they match by both name and type.
# 
# Input
# •	On the first line, you are given number N -> the number of dragons to follow.
# •	On the next N lines, you are given input in the above-described format. There will be a single space separating each element.
# 
# Output
# •	Print the aggregated data on the console.
# •	For each type, print average stats of its dragons in format "{type}::({damage}/{health}/{armor})".
# •	Damage, health, and armor should be rounded to two digits after the decimal separator.
# •	For each dragon, print its stats in format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}".
# 
# Constraints
# •	N is in range [1…100].
# •	The dragon type and name are one word only, starting with capital letter.
# •	Damage health and armor are integers in range [0 … 100000] or null.

dragons = {}
dtypes = []
default_stats = (45, 250, 10)

for _ in range(int(input())):
	dtype, name, dmg, hp, ac = input().split(' ')
	dmg, hp, ac = (default_stats[i] if x == 'null' else int(x) for i, x in enumerate((dmg, hp, ac)))
	
	key = (dtype, name)
	value = (dmg, hp, ac)
	dragons[key] = value
	
	if dtype not in dtypes:
		dtypes.append(dtype)
	
for dtype in dtypes:
	stats = [v for k, v in dragons.items() if k[0] == dtype]
	dmg, hp, ac = [sum(item) / len(item) for item in zip(*stats)]
	print(f'{dtype}::({dmg:.2f}/{hp:.2f}/{ac:.2f})')
	
	filtered_dragons = {k[1]: v for k, v in dragons.items() if k[0] == dtype}
	output = {k: v for k, v in sorted(filtered_dragons.items(), key= lambda item: item[0])}
	for k, v in output.items():
		print (f'-{k} -> damage: {v[0]}, health: {v[1]}, armor: {v[2]}')