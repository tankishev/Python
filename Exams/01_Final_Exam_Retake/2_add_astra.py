import re

pattern = r'(#|\|)([\w\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
food = []
total_calories = 0

input_line = input()

matches = re.finditer(pattern,input_line)
for m in matches:
    food.append((m.group(2),m.group(3),m.group(4)))
    total_calories += int(m.group(4))

print(f"You have food to last you for: {total_calories//2000} days!")
for item in food:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")




