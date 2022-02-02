# Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use an appropriate name for the function.

def smallest(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c

x = int(input())
y = int(input())
z = int(input())

print(smallest(x,y,z))