# Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to go home and you are the person who has to draw the line
#  and calculate the money from the products that were sold throughout the day. Until you receive a line with text "end of shift" you will be given lines of input. 
# But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# •	Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by lower-case letters
# •	Valid product contains any word character (not only letters) and must be surrounded by '<' and '>' 
# •	Valid count is an integer, surrounded by '|'
# •	Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}".
# Input / Constraints
# •	Strings that you have to process until you receive text "end of shift".
# Output
# •	Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
# •	After receiving "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}"
# •	Allowed working time / memory: 100ms / 16MB.

# name enclosed in %                                                    : ^%([A-Z][a-z]+)%
# potentially followed by random chars except ('|', '$', '%' and '.')   : (?:[^\.\|\$%]+)?
# followed by product enclosed in <>                                    : <(\w+)>
# potentially followed by random chars except ('|', '$', '%' and '.')   : (?:[^\.\|\$%]+)?
# followed by a sales count of integer enclosed in |                    : \|(\d+)\|
# potentially followed by random chars except ('|', '$', '%' and '.')   : (?:[^\.\|\$%]+)?
# followed by a real number ending with $                               : ((?<=\D)\d+(?:\.\d+)?\$)

import re

valid_order_old = r'^%([A-Z][a-z]+)%(?:[^\.\|\$%]+)?<(\w+)>(?:[^\.\|\$%]+)?\|(\d+)\|(?:[^\.\|\$%]+)?((?<=\D)\d+(?:\.\d+)?\$)'
valid_order = r'^%([A-Z][a-z]+)%(?:[^\.\|\$%]+)?<(\w+)>(?:[^\.\|\$%]+)?\|(\d+)\|(?:[^\.\|\$%]+)?((?<=\D)\d+(?:\.\d+)?)(?=\$)\$$'
income = 0

while True:
    text_input = input()
    if text_input == 'end of shift':
        break
    
    match = re.search(valid_order,text_input)

    if match:
        customerName = match.group(1)
        product = match.group(2)
        quantity = int(match.group(3))
        price = float(match.group(4))
        totalPrice = quantity * price
        print(f"{customerName}: {product} - {totalPrice:.2f}")
        income += totalPrice

print(f'Total income: {income:.2f}')