# On the first line, you will receive a number n. 
# On the second line, you will receive a word. 
# On the following n lines, you will be given some strings. 
# You should add them to a list and print them. 
# After that, you should filter out only the strings that include the given word and print that list too.

n = int(input())
word = input()
lst = []
for _ in range(n):
    lst.append(input())
print(lst)


#filtered_lst = [x for x in lst if x.find(word) >=0]
filtered_lst2 = [x for x in lst if word in x]

#print (filtered_lst)
print (filtered_lst2)


