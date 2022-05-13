command = input().split(" -> ")

database_dict = {}
failed_logins = 0

while command[0] != "login":
    username = command[0]
    password = command[1]
    database_dict[username] = password
    command = input().split(" -> ")

command = input().split(" -> ")

while command[0] != "end":
    username = command[0]
    password = command[1]
    if username in database_dict.keys() and password == database_dict[username]:
        print(f"{username}: logged in successfully")
    else:
        print(f"{username}: login failed")
        failed_logins += 1
    command = input().split(" -> ")

print(f"unsuccessful login attempts: {failed_logins}")
