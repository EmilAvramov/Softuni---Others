gift_list = str(input()).split(' ')
command = str(input())

temp_list = []

while command != "No Money":
    temp_list = command.split(' ')
    if "OutOfStock" in command:
        for i in range(len(gift_list)):
            if temp_list[1] in gift_list[i]:
                gift_list[i] = "None"
    elif "Required" in command:
        for i in range(len(gift_list)):
            if str(i) in command:
                if i == int(temp_list[2]):
                    gift_list[i] = temp_list[1]
    elif "JustInCase" in command:
        gift_list[-1] = temp_list[1]
    command = str(input())

while "None" in gift_list:
    gift_list.remove("None")

print(*gift_list, sep=" ")
