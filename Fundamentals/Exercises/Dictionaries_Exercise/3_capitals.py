# Using a dictionary comprehension, write a program that receives country names on the first line, separated by comma and space ", ", 
# and their corresponding capital cities on the second line (again separated by comma and space ", "). 
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".

capitals = {country: city for (country, city) in zip(input().split(', '), input().split(', '))}

for country, capital in capitals.items():
    print(f"{country} -> {capital}")