num_keys = [int(i) for i in input().split()]
command = input()

temp_string = ""
results = []
key_index = 0
keys = []
coordinates = []

while command != "find":
    for letter in command:
        temp_string += chr(ord(letter) - num_keys[key_index])
        key_index += 1
        if key_index == len(num_keys):
            key_index = 0
    results.append(temp_string)
    temp_string = ""
    key_index = 0
    command = input()

results = [i.split('&') for i in results]
keys = [i[1] for i in results]
coordinates = [i[-1].split("<")[-1][:-1] for i in results]

combined = list(zip(keys, coordinates))

for item in combined:
    print(f'Found {item[0]} at {item[1]}')
