# On the first line of the input, you will be given a text string. To win the competition, 
# you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), 
# they are a match, and you have to store them somewhere. Examples of mirror words: 
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"

# Input / Constraints
# •	You will recive a string.

# Output
# •	Print the proper output messages in the proper cases as described in the problem description.
# •	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# •	Each pair of mirror word must be printed with " <=> " between the words.

import re

pattern = r'(#|@)([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1'
matched_words = []
match_count = 0
line_input = input()

matches = re.finditer(pattern,line_input)

for m in matches:
    match_count += 1
    word_a, word_b = m.group(2), m.group(3)
    if word_a == word_b[::-1]:
        matched_words.append(f'{word_a} <=> {word_b}')

if match_count == 0:
    print("No word pairs found!")
else:
    print(f"{match_count} word pairs found!")

if not matched_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(*matched_words, sep=', ')

