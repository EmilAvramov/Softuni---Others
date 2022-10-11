i = 1
replace = ["-", ",", ".", "!", "?"]

with open("demofile.txt", "r") as f:
    for line in f.readlines():
        if i % 2 == 0:
            for letter in line:
                while letter in replace:
                    line.replace("@")
        print(line)
