# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and its coordinates. 
# 
# On the first line, you will receive a key (sequence of numbers separated by a space). 
# On the next few lines, you will receive lines with strings until you get the command "find". 
# 
# You should loop through every string and decrease the ASCII code of each character with a corresponding number of the key sequence. 
# You choose a key number from the sequence by just looping through it. 
# If the length of the key sequence is less than the string sequence, you should continue looping from the beginning. 
# 
# After decrypting the message, you will get a type of treasure and its coordinates. 
# The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'. 
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".


key = ''.join([x for x in input().split(' ')])

while True:
    encrypted_coordinates = input()
    if encrypted_coordinates == 'find':
        break
    
    while len(key) < len(encrypted_coordinates):
        key += key
    
    decrypted_coordinates = ''
    for i in range(len(encrypted_coordinates)):
        decrypted_coordinates += chr(ord(encrypted_coordinates[i]) - int(key[i]))
    
    treasure = decrypted_coordinates[decrypted_coordinates.find('&') + 1:]
    treasure = treasure[:treasure.find('&')]
    coordinates = decrypted_coordinates[decrypted_coordinates.find('<') + 1:decrypted_coordinates.find('>')]

    print(f'Found {treasure} at {coordinates}')
  