import re

re_clean_html = r"<p>(.+?)</p>"
re_replace = r"([^a-z0-9])"
re_rem_dup_space = r"\s{2,}"

temp_str = ""
result = []
data = input()

# clean HTML
clean_data = re.findall(re_clean_html, data)

# remove invalid chars
clean_data = [re.sub(re_replace, " ", str(i)) for i in clean_data]

# swap char sets via ASCII
for elem in clean_data:
    for letter in elem:
        if 97 <= ord(letter) <= 109:
            temp_str += chr(ord(letter) + 13)
        elif 110 <= ord(letter) <= 122:
            temp_str += chr(ord(letter) - 13)
        else:
            temp_str += letter
    result.append(temp_str)
    temp_str = ""

# replace dup spaces
result = [re.sub(re_rem_dup_space, " ", str(i)) for i in result]

print(''.join(result))
