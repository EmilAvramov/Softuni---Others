lines = int(input())

data_dict = {}

for line in range(lines):
    data = input()
    data_dict[data[data.index("@") + 1: data.index("|")]] = data[data.index("#") + 1: data.index("*")]

for key, value in data_dict.items():
    print(f'{key} is {value} years old.')
