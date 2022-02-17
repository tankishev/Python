# You will be given a sequence of strings, each on a new line. 
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
#  Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].

resources = {}
while True:
    resource = input()
    if resource == 'stop':
        break
    else:
        quantity = int(input())
        if resource not in resources:
            resources[resource] = 0
        resources[resource] += quantity

for item, qty in resources.items():
    print(f"{item} -> {qty}")