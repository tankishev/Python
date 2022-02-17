# You will be given series of strings until you receive an "end" command. Write a program that reverses strings and prints each pair on separate line in the format "{word} = {reversed word}".

while True:
    word = input()
    if word == 'end':
        break
    
    reversed_word = word[::-1]

    print(f"{word} = {reversed_word}")
