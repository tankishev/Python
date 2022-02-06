import re

pattern = r'(=|/)([A-Z][a-zA-Z]{2,}(?:\s[A-Z][a-zA-Z]{2,})?)\1'
dest = []
travel_points = 0

input_line = input()

matches = re.finditer(pattern, input_line)

for m in matches:
    destination = m.group(2)
    dest.append(destination)
    travel_points += len(destination)

print(f"Destinations:", ', '.join(dest))
print(f"Travel Points: {travel_points}")
