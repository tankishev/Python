bill = []
gross_price = 0

while True:
    line_input = input()
    if line_input.isalpha():
        break
    
    price = float(line_input)

    if price >= 0:
        gross_price += price
    else:
        print("Invalid price!")

if gross_price > 0:
    taxes = gross_price * 0.2
    total_price = taxes + gross_price
    if line_input == 'special':
        total_price *= 0.9

    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {gross_price:.2f}$')  
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f"Total price: {total_price:.2f}$")

else:
    print("Invalid order!")