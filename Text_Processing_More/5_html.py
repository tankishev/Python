# You will receive lines of input:
# •	On the first line, you will receive a title of an article
# •	On the second line, you will receive the content of that article
# •	On the following lines, until you receive "end of comments" you will get the comments about the article
# 
# Print the whole information in html format:
# •	The title should be in "h1" tag (<h1></h1>)
# •	The content in article tag (<article></article>)
# •	Each comment should be in div tag (<div></div>)
# For more clarification see the example below.

title = input()
content = input()
comments = []

while True:
    comment = input()
    if comment == 'end of comments':
        break

    comments.append(comment)

print (f'<h1>\n\t{title}\n</h1>\n<article>\n\t{content}\n</article>')
for comment in comments:
    print(f'<div>\n\t{comment}\n</div>')