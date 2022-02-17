# You seem to be doing great at your first job, so your boss decides to give you as your next task something more challenging. 
# You have to accept all the new products coming in the bakery and finally gather some statistics.
# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". 
# Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one. 
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

bakery_products = {}
while True:
    input_line = input()
    if input_line == 'statistics':
        break
    
    else:
        product_qty = input_line.split(': ')
        product = product_qty[0]
        quantity = int(product_qty[1])
        if product in bakery_products:
            bakery_products[product] += quantity
        else:
            bakery_products[product] = quantity

print("Products in stock:")    
for prod, qty in bakery_products.items():
    print(f'- {prod}: {qty}')
print(f"Total Products: {len(bakery_products)}\nTotal Quantity: {sum(bakery_products.values())}")    

