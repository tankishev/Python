# It is time to get in a Christmas mood. You need to decorate the house in time for the big event, but you have limited days to do so.
# You will receive an allowed quantity for one type of decoration and days left until Christmas day to decorate the house.

# There are 4 types of decorations, and each piece costs a price
# •	Ornament Set – 2$ per piece
# •	Tree Skirt – 5$ per piece
# •	Tree Garlands – 3$ per piece
# •	Tree Lights – 15$ per piece

# Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
# Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
# Every fifth day you buy Tree Lights and increase your Christmas spirit by 17. 
# If you have bought Tree Skirts and Tree Garlands on the same day, you additionally increase your spirit by 30.
# Every tenth day you lose 20 points of the spirit because your cat ruins all tree decorations, and you should rebuild the tree and buy one piece of tree skirt, garlands, and lights. 
# That is why you are forced to increase the allowed quantity with 2 at the beginning of every eleventh day.
# Also, if the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey, and you lose an additional 30 points of spirit.
# In the end, you must print the total cost and the gained spirit.

# Input / Constraints
# The input will consist of exactly 2 lines:
# •	quantity – integer in the range [1…100]
# •	days – integer in the range [1…100]

# Output
# In the end, print the total cost and the total gained spirit in the following format:
# •	"Total cost: {budget}"
# •	"Total spirit: {totalSpirit}"

# Examples
# Input	Output
# 1
# 7	Total cost: 37
# Total spirit: 58 
# 3
# 20	Total cost: 558
# Total spirit: 156


price_ornament = 2
price_tree_skirt = 5
price_garlands = 3
price_lights = 15

quantity = int(input())
days = int(input())

budget = 0
totalSpirit = 0

for i in range(1 , days + 1):
    if (i % 11) == 0:
        quantity += 2

    # Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
    if (i % 2) == 0:
        budget += quantity * price_ornament  
        totalSpirit += 5
    # Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
    if (i % 3) == 0:
        budget += quantity * (price_garlands + price_tree_skirt)
        totalSpirit += 13 

    # Every fifth day you buy Tree Lights and increase your Christmas spirit by 17. 
    if (i % 5) == 0:
        budget += price_lights * quantity
        totalSpirit += 17

    # If you have bought Tree Skirts and Tree Garlands on the same day, you additionally increase your spirit by 30.
    if (i % 15) == 0:
        totalSpirit += 30

    # Every tenth day you lose 20 points of the spirit because your cat ruins all tree decorations, and you should rebuild the tree and buy one piece of tree skirt, garlands, and lights. 
    # That is why you are forced to increase the allowed quantity with 2 at the beginning of every eleventh day.
    # Also, if the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey, and you lose an additional 30 points of spirit.
    if (i % 10) == 0:
        budget += price_tree_skirt + price_garlands + price_lights 
        totalSpirit -= 20

        if i == days:
            totalSpirit -= 30
    
print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")