# ulates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are: 
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00

# Print the result formatted to the second decimal place.

# constants
price_list = {
    'coffee': 1.50,
    'water': 1.00,
    'coke': 1.40,
    'snacks': 2.00
}

# defined functions
def bill(order, number):
    cost = price_list[order] * number
    return cost

# main code
order = input()
quantity = int(input())

print('{:.2f}'.format(bill(order,quantity)))