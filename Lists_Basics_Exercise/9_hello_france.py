# You want to go to France by train, and the train ticket costs exactly 150$. 
# You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# 
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# 
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	        Maximum Price
# Clothes	    50.00
# Shoes	        35.00
# Accessories	20.50
# 
# If a price for a particular item is higher than the maximum price, don't buy it. 
# Every time you buy an item, you have to reduce the budget with its price value. 
# If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# 
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. 
# Calculate if the budget after selling all the items is enough for buying the train ticket.

# Input / Constraints
# •	On the 1st line, you will receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
# •	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]

# Output
# •	First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
# "{price1} {price2} {price3} … {priceN}"
# •	Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# •	Finally:
# o	If the budget is enough for buying the train ticket, print: "Hello, France!" 
# o	Otherwise, print: "Not enough money."

train_ticket = 150

max_price = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50
}

item_list = input().split('|')
starting_budget = float(input())
remaining_budget = starting_budget

item_list = [item.split('->') for item in item_list]
for item in item_list:
    item[1] = float(item[1])

fitered_list = list(filter(lambda item: item[1] <= max_price[item[0]],item_list))

sales_list = []
for item in fitered_list:
    if item[1] <= remaining_budget:
        remaining_budget -= item[1]
        sales_list.append(item[1])

profit = sum([x * 0.4 for x in sales_list])
print_list = ['{:.2f}'.format(x * 1.4) for x in sales_list]

starting_budget += profit

print(*print_list, sep=' ')
print(f'Profit: {profit:.2f}')
if starting_budget >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')