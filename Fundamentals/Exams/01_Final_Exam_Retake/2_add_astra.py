# You are an astronaut who just embarked on a mission across the solar system. 
# Since you will be in space for a long time, you have packed a lot of food with you. Create a program, 
# which helps you identify how much food you have left and gives you information about its expiration date.
# On the first line of the input, you will be given a text string. 
# You must extract the information about the food and calculate the total calories. 
# 
# First, you must extract the food info. It will always follow the same pattern rules:
# •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern: 
# #{item name}#{expiration date}#{calories}#   or 
# |{item name}|{expiration date}|{calories}|
# •	The item name will contain only lowercase and uppercase letters and whitespace
# •	The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long
# •	The calories will be an integer between 0-10000
# 
# Calculate the total calories of all food items and then determine how many days you can last with the food you have. Keep in mind that you need 2000kcal a day.
# 
# Input / Constraints
# •	You will receive a single string
# 
# Output
# •	First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
# •	The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"

import re

pattern = r'(#|\|)([\w\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
food = []
total_calories = 0

input_line = input()

matches = re.finditer(pattern, input_line)
for m in matches:
    food.append((m.group(2), m.group(3), m.group(4)))
    total_calories += int(m.group(4))

print(f"You have food to last you for: {total_calories//2000} days!")
for item in food:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")




