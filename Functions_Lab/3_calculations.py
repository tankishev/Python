# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the following:  "multiply", "divide", "add", "subtract". 


def calc(operation, num_a, num_b):
    if operation == "multiply":
        result =  num_a * num_b
        return result
    elif operation == "divide" and num_b != 0:
        result =  num_a / num_b
        return result
    elif operation == "add":
        result =  num_a + num_b
        return result
    elif operation == "subtract":
        result =  num_a - num_b
        return result

operation = input()
num_a = int(input())
num_b = int(input())
print('{:.0f}'.format(calc(operation,num_a,num_b)))