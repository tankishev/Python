# You work at a coffee shop, and your job is to place orders to the distributors. Thus, you want to know the price of each order. On the first line, you will receive integer N – the number of orders the shop will receive. For each order, you will receive the following information:
# •	Price per capsule - a floating-point number in the range [0.00…1000.00]
# •	Days – integer in the range [1…31]
# •	Capsules count - integer in the range [0…2000]
# For each order, you should print a single line in the following format:
# •	"The price for the coffee is: ${price}"
# On the final line, you need to print the total price in the following format:
# •	 "Total: ${total_price}"
# The price must be formatted to the second decimal place. 

totalcost = 0
n = int(input())
for i in range(n):
    p = float(input())
    d = int(input())
    c = int(input())
    cost = p*d*c
    totalcost += cost
    cost = "{:.2f}".format(cost)
    print(f"The price for the coffee is: ${cost}")

totalcost = "{:.2f}".format(totalcost)
print(f"Total: ${totalcost}")