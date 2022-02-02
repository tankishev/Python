# Write a function that receives two integer numbers. Calculate the factorial of each number. 
# Divide the first result by the second and print the division formatted to the second decimal point.


def factorial_division(x,y):
    def factorial(x):
        output = x
        for i in range(2,x):
            output *= i
        return output

    fact_x = factorial(x)
    fact_y = factorial(y)

    output = fact_x / fact_y
    return output

int_a = int(input())
int_b = int(input())

if int_a > 0 and int_b > 0:
    result = factorial_division(int_a,int_b)
    print('{:.2f}'.format(result))