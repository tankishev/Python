# Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
# Create a program that calculates how many loaves you can make with the budget you have.
#  First, you will receive your budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one bread:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l

# The price for 1 pack of eggs is 75% of the price for 1 kg flour. 
# The price for 1l milk is 25% more than the price for 1 kg flour. 
# Notice that you need 0.250l milk for one bread, and the calculated price is for 1l.

# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
# •	For every bread that you make, you will receive 3 colored eggs. 
# •	For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs for your bread. The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves – ({current_bread_count} – 2)
# In the end, print the loaves of bread you made, the eggs you have gathered, and the money you have left, formatted to the 2nd decimal place, in the following format:
# "You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."

# Input / Constraints
# •	On the 1st line, you will receive the budget – a real number in the range [0.0…100000.0]
# •	On the 2nd line, you will receive the price for 1 kg flour – a real number in the range [0.0…100000.0]
# •	The input will always be in the correct format
# •	You will always have a remaining budget
# •	There will not be a case in which the eggs become a negative count

# Output
# •	In the end, print the number of Easter bread you have made, the colored eggs you have gathered, and the money formatted to the 2nd decimal place in the format described above.

# Examples
# Input	Output
# 20.50
# 1.25	You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left.
# 15.75
# 1.4	You made 5 loaves of Easter bread! Now you have 14 eggs and 1.31BGN left.


budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
price_bread = price_flour + price_eggs + price_milk / 4 
number_of_bread = 0
number_of_coloured_eggs = 0

while budget >= price_bread:
    budget -= price_bread
    number_of_bread += 1
    number_of_coloured_eggs += 3
    if (number_of_bread % 3) == 0:
        number_of_coloured_eggs -= (number_of_bread - 2)
else:
    print(f"You made {number_of_bread} loaves of Easter bread! Now you have {number_of_coloured_eggs} eggs and {budget:.2f}BGN left.")
