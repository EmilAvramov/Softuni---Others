phone = input().split(" : ")

phone_dict = {}

while phone[0] != "Over":
    if phone[0].isnumeric():
        phone_dict[phone[1]] = phone[0]
    else:
        phone_dict[phone[0]] = phone[1]
    phone = input().split(" : ")

for key, value in sorted(phone_dict.items()):
    print(f'{key} -> {value}')
