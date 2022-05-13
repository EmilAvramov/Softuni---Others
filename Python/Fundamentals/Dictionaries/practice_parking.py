def call_register(_username, _license, _dict):
    if _username in _dict:
        return f'ERROR: already registered with plate number {_license}'
    else:
        _dict[_username] = _license
        return f'{_username} registered {_license} successfully'


def call_unregister(_username, _dict):
    if _username not in _dict:
        return f'ERROR: user {_username} not found'
    else:
        del _dict[_username]
        return f'{_username} unregistered successfully'


commands = int(input())

parking_db = {}

for i in range(commands):
    operation = input().split()
    if operation[0] == "register":
        print(call_register(operation[1], operation[2], parking_db))
    elif operation[0] == "unregister":
        print(call_unregister(operation[1], parking_db))

for key, value in parking_db.items():
    print(f'{key} => {value}')
