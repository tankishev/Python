# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers (integers) as additional arguments (*args). The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below. 
# Submit only your function in the Judge system.


def operate(operator, *args):
    result = args[0]

    calc = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b  if b !=0 else a
    }

    for num in args[1:]:
        result = calc[operator](result,num)
    
    return result

print(operate("*", 3, 4))