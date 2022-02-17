# Create a function called age_assignment that receives a different number of names and a different number of key-value pairs. 
# The key will be a single letter (the first letter of each name) and the value - a number (age). 
# Find its first letter in the key-value pairs for each name and assign the age to the person's name. 
# It the end, return a dictionary with all the names and ages as shown in the example. 
# Submit only the function in the judge system.

def age_assignment(*args, **kwargs):
    return {arg: kwargs.get(arg[0]) for arg in args}

