# Using comprehension, write a program that receives some text, separated by space, and take only those words whose length is even. Print each word on a new line.

input_words = [word for word in input().split(' ')]
filtered_list = list(filter(lambda word: len(word) % 2 == 0, input_words))
for word in filtered_list:
    print(word)
