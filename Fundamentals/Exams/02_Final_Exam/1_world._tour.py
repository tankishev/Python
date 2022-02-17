# On the first line, you will be given a string containing all of your stops. 
# Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"

# Input / Constraints
# •	JavaScript: you will receive a list of strings
# •	An index is valid if it is between the first and the last element index (inclusive) in the sequence.

# Output
# •	Print the proper output messages in the proper cases as described in the problem description


stops = input()
while True:
    input_line = input()
    if input_line == 'Travel':
        break

    tokens = input_line.split(':')
    command = tokens[0]

    if command == 'Add Stop':
        i = int(tokens[1])
        stop = tokens[2]
        
        if 0 <= i < len(stops):
            stops = stops[:i] + stop + stops[i:]

        print(stops)
        
    elif command == 'Remove Stop':
        i = int(tokens[1])
        j = int(tokens[2])

        if 0 <= min(i,j) and max(i,j) < len(stops):
            stops = stops[:i] + stops[j+1:]
        
        print(stops)
        
    elif command == 'Switch':
        old_str = tokens[1]
        new_str = tokens[2]

        if len(old_str) > 0 and len(new_str) > 0:
            stops = stops.replace(old_str, new_str)
            print(stops)

print(f"Ready for world tour! Planned stops: {stops}")