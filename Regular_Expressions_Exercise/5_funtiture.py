# Write a program that calculates the total cost of bought furniture. 
# You will be given information about each purchase on separate lines until you receive the command "Purchase". 
# 
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". 
# The price could be a floating-point or integer number. You should store the names of the furniture and the total price. 
# 
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

import re
# r'^>>([a-zA-Z]+)<<(\d+(\.\d{2})?)!(\d+)$'
valid_pattern = re.compile(r'^>>([a-zA-Z]+)<<(\d+(\.\d+)?)!(\d+)$')
bought_furniture = []
total_cost = 0

while True:
    input_text = input()
    if input_text == 'Purchase':
        break
    
    match = valid_pattern.search(input_text)
    if match:
        bought_furniture.append(match.group(1))
        total_cost += float(match.group(2)) * int(match.group(4))
    

print('Bought furniture:')
for item in bought_furniture:
    print(item)
print(f'Total money spend: {total_cost:.2f}')
