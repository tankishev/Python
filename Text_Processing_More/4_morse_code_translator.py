# Write a program that translates messages from Morse code to English (capital letters). 
# Use this page to help you (without the numbers). The words will be separated by a space (' '). Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.

morse_code_dict = { '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z'}

morse_words_list = [str(word).strip() for word in input().split(' | ')]

output = []

for morse_word in morse_words_list:
    english_word = ''.join([morse_code_dict[morse_char] for morse_char in morse_word.split(' ')])
    output.append(english_word)


print(' '.join(output))