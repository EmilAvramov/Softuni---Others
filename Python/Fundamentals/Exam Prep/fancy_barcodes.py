import re

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

count = int(input())

for i in range(count):
    data = input()
    result = re.findall(pattern, data)
    if result:
        sum_digits = ""
        for i in range(len(result[0])):
            if result[0][i].isdigit():
                sum_digits += result[0][i]
        if sum_digits == "":
            sum_digits = "00"
        print(f"Product group: {sum_digits}")
        sum_digits = ""
    else:
        print("Invalid barcode")
