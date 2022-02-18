# Write a function called stock_availability which receives:
# •	an inventory list of boxes with different kinds of cupcake flavours
# •	"delivery" or "sell" as second parameter
# •	there might or might not be any other parameters – numbers or strings at the end

# In case of "delivery"  to the shop was delivered new boxes with diferent kinds of cupcakes:
# •	You should add the boxes at the end of the inventory list
# •	There will be always at least one box delivered
# In case of "sell" Maria has a client and she is selling different boxes with cupcakes:
# •	If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes and you should remove them from the beginning of the inventory list
# •	If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes of the ordered flavour/s. Beware that not everything the buyer has ordered might be in stock, so you should check if the order is valid.  
# •	If there are no other parameters, it means that Maria has sold only the first box of cupcakes and you should remove  it of the inventory list
# For more clarifications, see the examples below.
# Input
# •	There will be no input
# •	Parameters will be passed to your function
# Output
# •	The function should return a new inventory list
# •	All commands will be valid


from collections import deque


def stock_availability(boxes: list, delivery_sell: str, *args):
    inventory = deque(boxes)

    if delivery_sell == 'delivery':
        inventory.extend([arg for arg in args])
    
    elif delivery_sell == 'sell':
        if inventory and not args:
            inventory.popleft()

        elif len(args) == 1 and type(args[0]) == int:
            for _ in range(int(args[0])):
                if inventory:
                    inventory.popleft()

        else:
            for arg in args:
                while inventory and arg in inventory:
                    inventory.remove(arg)

    return [el for el in inventory]
