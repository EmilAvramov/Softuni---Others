import re

data = input()
re_filter = r"\W*(\w+)\W*"
re_replace = r"\+|%20"
re_split = r"&|\?"

data_dict = {}

while data != "END":
    clean_data = re.sub(re_replace, "|", data)
    clean_data = re.split(re_split, clean_data)
    for data in clean_data:
        if "=" in data:
            data = data.split("=")
            key = re.findall(re_filter, data[0])[0]
            if "http" not in data[1]:
                value = re.findall(re_filter, data[1])
                value = ' '.join(value)
            else:
                value = data[1]
            if key not in data_dict.keys():
                data_dict[key] = [value]
            else:
                data_dict[key] += [value]
    for key, value in data_dict.items():
        print(f"{key}=[{', '.join(value)}]", end='')
    print()
    data_dict = {}
    data = input()
