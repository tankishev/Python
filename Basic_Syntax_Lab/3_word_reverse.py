word = input()
res = ''
for i in reversed(range(len(word))):
    res += word[i]

print(res)