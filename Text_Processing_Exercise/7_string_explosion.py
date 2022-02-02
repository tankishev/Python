# Write a program that reads a string from the console that contains:
# •	Explosions marked with '>'
# •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# •	Any other characters
# 
# Your task is to delete x characters, starting after the exploded character ('>'). 
# If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion. 
# You should not delete the explosion character – '>'.
# 
# When all characters are processed, print the final string. 
# Constraints
# •	You will always receive strength for the explosions
# •	The path will consist only of letters from the Latin alphabet, integers, and the char '>'
# •	The strength of the punches will be in the interval [0…9]


input_string = input()
index = 0
explosion = 0

while index < len(input_string):
    char = input_string[index]
    if input_string[index] == '>':
        explosion += int(input_string[index + 1])
        index += 1

    elif explosion > 0:
        input_string =  input_string[:index] + input_string[index + 1:]
        explosion -= 1

    else:
        index += 1
else:
    print(input_string)

