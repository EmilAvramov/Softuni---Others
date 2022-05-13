username = input()
password = input()
user_data = input()

while user_data != password:
    user_data = input()

print(f'Welcome {username}!')