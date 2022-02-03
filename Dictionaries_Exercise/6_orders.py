# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. 
# Finally, print all items with their names and the total price of each product. 
# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.
# Output
# •	Print information about each product in the following format: 
# "{product_name} -> {total_price}"
# •	Format the total price to the 2nd digit after the decimal separator.

products = {}

while True:
    input_line = input()
    if input_line == 'buy':
        break
    
    name, price, quantity = input_line.split(' ')
    if name not in products:
        products[name] = {'price': float(price), 'quantity': int(quantity)}
    else:
        products[name]['price'] = float(price)
        products[name]['quantity'] += int(quantity)

for product_name in products:
    total_price = products[product_name]['price'] * products[product_name]['quantity']
    print(f"{product_name} -> {total_price:.2f}")