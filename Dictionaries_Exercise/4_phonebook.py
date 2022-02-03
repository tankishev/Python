# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N. 
# Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}". 
# In case the contact isn't found, print: "Contact {name} does not exist."

contacts = {}

while True:
    input_line = input()
    if input_line.isnumeric():
        break
    name, number = input_line.split('-')
    contacts[name] = number

for _ in range(int(input_line)):
    search_name = input()
    if search_name in contacts:
        print(f"{search_name} -> {contacts[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")