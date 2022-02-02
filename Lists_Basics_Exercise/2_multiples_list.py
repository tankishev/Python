# Write a program that receives two numbers (factor and count). 
# It should create a list with a length of the given count that contains only integer numbers, 
# which are multiples of the given factor. 
# The numbers should be only positive, and they should be arranged in ascending order, 
# starting from the value of the factor.

factor = int(input())
count = int(input())
lst = []

# for i in range(1, count + 1):
#     lst.append(i * factor)
# print(lst)

lst2 = [x * factor for x in range(1, count + 1)]
print(lst2)

# тъжна е гората в късна есен.
# клоните на дърветата стърчат черни и безмълвни.
# не полъхва вятър.
# вървиш и мълчиш.
# стъпките ти едва се чуват.
# краката ти потъват в мека шума.
# очите ти не виждат билка или пъстър цвят.
# не подвиква от никъде птица.
# повечето от тях отдавна са улетели на юг.
# а как беше красива гората в топлите дни!
# седя замислен на дънера и ми става до болка тъжно, че гората е глуха и пуста.
# кога ще падне сняг, та всичко да е бяло, хубаво, чисто?