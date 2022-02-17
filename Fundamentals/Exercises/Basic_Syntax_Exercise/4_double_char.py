# You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.
# Examples
# Input	Output
# Hello World	HHeelllloo  WWoorrlldd
# 1234!	11223344!!

txt = input()
res = ''
for i in range(len(txt)):
    res += txt[i]*2
print(res)