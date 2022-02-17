# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits 
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def validate_password(password):
    password_valid = True
    if not (6 <= len(password) <= 10):
        print('Password must be between 6 and 10 characters')
        password_valid = False

    for char in password:
        if char not in charset:
            print("Password must consist only of letters and digits")
            password_valid = False
            break
    
    count = 0
    for char in password:
        if char in '0123456789':
            count +=1
    if count < 2:
        print("Password must have at least 2 digits")
        password_valid = False
    

    if password_valid:
        print("Password is valid")

password = input()
validate_password(password)
