command = str(input()).split('-')

# Method 1, append list, sort and extract values into separate list by their index
activity_list = []
sorted_list = []

while command[0] != "End":
    activity_list.append(command)
    command = str(input()).split('-')

activity_list = sorted([[int(i) if i.isdigit() else i for i in elements] for elements in activity_list])
sorted_list = [i[1] for i in activity_list]

print(sorted_list)

# Method 2, using pop() and insert()
# activity_list = ['placeholder'] * 10
#
# while command[0] != "End":
#     activity_list.pop(int(command[0]) - 1)
#     activity_list.insert(int(command[0]) - 1, command[1])
#     command = str(input()).split('-')
#
# activity_list = [i for i in activity_list if i != 'placeholder']
#
# print(activity_list)
