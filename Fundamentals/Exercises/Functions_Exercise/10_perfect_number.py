# A perfect number is a positive integer that is equal to the sum of its proper positive divisors. 
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def test_perfect_number(number):
    if number > 0:
        test_sum = 0
        for i in range(1,number + 1 // 2):
            if (number % i) == 0:
                test_sum += i

    if number == test_sum:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

number = int(input())
test_perfect_number(number)
