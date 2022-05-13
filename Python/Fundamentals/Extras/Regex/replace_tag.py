import re

re_find = r"<a.*?href.*?=(.*)>(.*?)<\/a>"
re_replace = r"[URL href=\1]\2[/URL]"

data = input()

while data != "end":
    match = re.findall(re_find, data)
    if match:
        data = re.sub(re_find, re_replace, data)
    print(data)
    data = input()
