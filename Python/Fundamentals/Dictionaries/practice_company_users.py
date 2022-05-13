company_dict = {}

command = input().split(' -> ')

while command[0] != "End":
    company = command[0]
    employee = command[1]
    if company not in company_dict:
        company_dict[company] = [employee]
    else:
        if employee not in company_dict[company]:
            company_dict[company] += [employee]
    command = input().split(' -> ')

for key, value in company_dict.items():
    print(key)
    for key_sub, value_sub in company_dict.items():
        for i in range(len(value_sub)):
            if key_sub in key:
                print(f'-- {value_sub[i]}')