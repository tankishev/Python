# You will receive a list of the cutomers (numbers seperated by comma and space ", ") on the first line and list of your taxis (numbers seperated by comma and space ", ").
# Each number from the customer list represents how much time it takes to drive the customer to his/her destination.
# Each number from the taxis list represents how much time they can drive, before they need to refill their tanks.
# Keep track of the total time passed to drive all the customers to their destinations (values of all customers).
# Each time you tend customers you should put the first customer in the last taxi until there are no customers left.
# •	If the taxi can drive the customer to his/her destination, he does and you must add the time passed to drive the customer to his/her destination (the value of the current customer) to the total time.
# Remove both the customer and the taxi.
# •	If the taxi cannot drive the customer to his/her destination, leave the customer at the beginning of the queue and remove the taxi.
# At the end if you have successfully driven all the customers to their destinations, print
# All customers were driven to their destinations
# Total time: {total_time} minutes
# Otherwise, if you ran out of taxis and there are still some customers left print
# Not all customers were driven to their destinations
# Customers left: {left_customers joined by ", "}
# Input
# •	On the first line you are given the customers – numbers seperated by comma and space ", "
# •	On the second line you are given the taxis – numbers seperated by comma and space ", "
# Output
# •	Print the output as described above


from collections import deque

customers = deque([int(el) for el in input().split(', ')])
taxis = deque([int(el) for el in input().split(', ')])
total_time = 0

while customers and taxis:
    if customers[0] <= taxis[-1]:
        total_time += customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
elif not taxis:
    print('Not all customers were driven to their destinations')
    print('Customers left: ', ", ".join([str(el) for el in customers]), sep='')
