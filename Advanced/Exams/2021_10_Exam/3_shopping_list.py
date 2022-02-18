# Write a function called shopping_list which will receive an integer number representing the budget in leva and a different number of keywords. Each key represents the product (string), and each value will be a tuple with the product's price (integer or float number) at the first position and quantity (integer) at the second position.
# Your job is to return which products you bought with the given budget. You only buy a product if you can buy all of its quantity.
# You could only start shopping if you have at least 100 leva budget. Otherwise, you should stop the program and return "You do not have enough budget.".
# Also, you are carrying a basket that cannot hold more than 5 types of products. You should stop buying products:
# •	if you reach the allowed amount of types of products (no matter their quantity)
# •	if you did not reach the allowed amount, but you do not have more products on the shopping list
# You should always buy products successively!
# For each product (all its quantity) you succeeded to buy, return a string on a new line in the following format:
# "You bought {product_name} for {total_price} leva."
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, and just parameters passed to your function
# Output
# •	The function should return strings on separate lines containing the bought products and their price in the format described above.
# •	The total price should be formatted to the second decimal point.


def shopping_list(budget: int, **kwargs) -> str:
    if budget < 100:
        return 'You do not have enough budget.'

    basket = []
    for name, val in kwargs.items():

        cost = float(val[0]) * int(val[1])

        if cost <= budget:
            budget -= cost
            basket.append((name, cost))

        if budget == 0 or len(basket) == 5:
            break

    output = ''
    for item in basket:
        output += f'You bought {item[0]} for {item[1]:.2f} leva.\n'

    return output[:-1]
