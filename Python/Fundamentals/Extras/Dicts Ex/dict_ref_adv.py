data = input()

data_dict = {}

while data != "end":
    dict_key = data.split(" -> ")[0]
    dict_val = [int(i) if i.isnumeric() else i
                for i in data.split(" -> ")[1].split(", ")]
    if isinstance(dict_val[0], int):
        if dict_key not in data_dict.keys():
            data_dict[dict_key] = dict_val
        else:
            for value in dict_val:
                if value not in data_dict[dict_key]:
                    data_dict[dict_key].append(value)
    else:
        if dict_val[0] in data_dict.keys():
            """ Circular references
            Create as empty list first as to avoid circular loop --
            when you modify the reference value, the created
            value also gets modified in the same manner if you do
            data_dict[dict_key] = data_dict[dict_val[0]]
            """
            data_dict[dict_key] = []
            data_dict[dict_key] += data_dict[dict_val[0]]
    data = input()

for key, value in data_dict.items():
    print(f"{key} === ", end='')
    print(*value, sep=', ')
