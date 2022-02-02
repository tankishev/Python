# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# •	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# •	The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old." 
# For each found name-age pair, print a line in the following format "{name} is {age} years old."


#  '@(\w+)(?=\|)(?:.+)?#(\d+)(?=\*)'

n = int(input())
name = None
age = None
for _ in range(n):
    input_string = input()
    
    temp_string = input_string

    name_start_index = temp_string.find('@', None)
    
    if name_start_index >= 0 and name_start_index < len(temp_string):
        temp_string = temp_string[name_start_index +1:]
        
        name_end_index = temp_string.find('|', None)

        if name_end_index >= 0:
            name = temp_string[:name_end_index]
        
    temp_string = input_string

    age_start_index = temp_string.find('#', None)
    
    if age_start_index >= 0 and age_start_index < len(temp_string):
        temp_string = temp_string[age_start_index +1:]
        
        age_end_index = temp_string.find('*', None)

        if age_end_index >= 0:
            age = temp_string[:age_end_index]
        
    
    if name and age:
        print(f'{name} is {age} years old.')

