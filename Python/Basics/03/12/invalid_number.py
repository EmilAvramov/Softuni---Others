number = int(input())

#if 100 <= number <= 200 or number == 0:
   # value = "valid"
#else:
    #value = "invalid"
   # print("invalid")

valid = 100 <= number <= 200 or number == 0
if not valid:
    print("invalid")