title = input()
content = input()
comments = input()

comment_list = []

while comments != "end of comments":
    comment_list.append(comments)
    comments = input()

print(f'<h1>')
print(f'    {title}')
print(f'</h1>')
print(f'<article>')
print(f'    {content}')
print(f'</article>')
for comment in comment_list:
    print(f'<div>')
    print(f'    {comment}')
    print(f'</div>')