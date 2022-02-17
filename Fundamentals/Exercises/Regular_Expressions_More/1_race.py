import re

racer_names = input()

race_results = {racer: 0 for racer in racer_names.split(', ')}

name_pattern = re.compile(r'[a-zA-Z]+')
distance_pattern = re.compile(r'[0-9]')
while True:
    input_string = input()
    if input_string == 'end of race':
        break
    
    name_match = name_pattern.findall(input_string)
    distance_match = distance_pattern.findall(input_string)
        
    if name_match and distance_match:
        name = ''.join(name_match)
        distance = sum([int(x) for x in distance_match])
        if name in race_results.keys():
            race_results[name] += distance
    
sorted_results = sorted(race_results.items(), key=lambda x: x[1], reverse=True)

print (f'1st place: {sorted_results[0][0]}\n2nd place: {sorted_results[1][0]}\n3rd place: {sorted_results[2][0]}')