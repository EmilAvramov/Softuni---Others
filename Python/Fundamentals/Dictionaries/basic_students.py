command = input().split(":")
student_dict = {}

while command[0].islower() is False:
    student_dict[command[0]] = int(command[1]), command[2]
    command = input().split(":")

for key, value in student_dict.items():
    if command[0] in value:
        print(f'{key} - {value[0]}')
    elif ''.join(command[0].split("_")) in ''.join(str(value).split()):
        print(f'{key} - {value[0]}')