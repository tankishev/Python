# Beaches are filled with sand, water, fish, and sun. 
# Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).

input_str = input().lower()
given_words = ('Sand','Water','Fish','Sun')
word_list = [x.lower() for x in given_words]
word_chr = [x[:2] for x in word_list]


count = 0
i = 0

while i < len(input_str):
    loop_chr = input_str[i:i+2]
    if loop_chr in word_chr:
        word_index = word_chr.index(loop_chr)
        word_len = len(word_list[word_index])
        if input_str[i:i+word_len] in word_list:
            count += 1
            i += word_len 
            continue
    i += 1

print(count)