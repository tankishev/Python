# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky. Create a program that receives an age and prints what they drink.
# Rules:
# A kid is defined as someone under the age of 14.
# A teen is defined as someone under the age of 18.
# A young adult is defined as someone under the age of 21.
# An adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!

num = int(input())
if num < 15:
    print('drink toddy')
elif num < 19:
    print('drink coke')
elif num < 22:
    print('drink beer')
else:
    print('drink whisky')