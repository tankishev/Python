def reverse_text(input_text: str) -> iter:
    i = len(input_text)
    while i > 0:
        i -= 1
        yield input_text[i]


for char in reverse_text("step"):
    print(char, end='')
