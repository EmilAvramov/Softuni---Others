string_A = str(input())
string_B = str(input())

list_A = []
list_B = []
concat_A = ""

for char_A in string_A:
    list_A += char_A

for char_B in string_B:
    list_B += char_B

for i in range(0, len(list_A)):
    if list_A[i] != list_B[i]:
        list_A[i] = list_B[i]
        for x in list_A:
            concat_A += x
        print(concat_A, end='\n')
        concat_A = ""
