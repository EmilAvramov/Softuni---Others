command = input().split(" -> ")

employee_dict = {}

while command[0] != "filter base":
    name = command[0]
    parameter = command[1]
    if name in employee_dict.keys():
        if parameter.isalpha():
            employee_dict[name].update({"Position": parameter})
        elif parameter.isdecimal():
            employee_dict[name].update({"Age": int(parameter)})
        else:  # float
            employee_dict[name].update({"Salary": float(parameter)})
    else:
        if parameter.isalpha():
            employee_dict[name] = {"Position": parameter}
        elif parameter.isdecimal():
            employee_dict[name] = {"Age": int(parameter)}
        else:  # int
            employee_dict[name] = {"Salary": float(parameter)}
    command = input().split(" -> ")

filter_data = input()

for key, value in employee_dict.items():
    for sub_key, sub_value in value.items():
        if filter_data in sub_key:
            print(f"Name: {key}")
            print(f"{filter_data}: {sub_value}")
            print("====================")
