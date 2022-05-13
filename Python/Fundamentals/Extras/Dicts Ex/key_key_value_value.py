main_dict = {input(): input()}
count = int(input())

data_dict = {}

for i in range(count):
    string = input().split(" => ")
    data_key = string[0]
    data_values = string[1].split(";")
    data_dict[data_key] = data_values

for data_key, data_value in data_dict.items():
    for main_key, main_value in main_dict.items():
        if main_key in str(data_key):
            print(f"{data_key}:")
            for data in data_value:
                if main_value in data:
                    print(f"-{data}")
