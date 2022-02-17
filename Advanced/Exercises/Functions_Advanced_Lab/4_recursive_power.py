def recursive_power(number:int, power:int):
    output = number
    if power > 1:
        output *= recursive_power(number, power - 1)
    
    return output


print(recursive_power(2, 10))