def command_split(_string, _command, _operator):
    if "|" in _string:
        _command.clear()
        _command.append(_string.split(" | ")[0])
        _command.append(_string.split(" | ")[1])
        _operator.clear()
        _operator.append("|")
    else:
        _command.clear()
        _command.append(_string.split(" -> ")[0])
        _command.append(_string.split(" -> ")[1])
        _operator.clear()
        _operator.append("->")


def user_exists(_user, _dict):
    if any(_user in val for val in _dict.values()):
        return True
    else:
        return False


def delete_user(_user, _force, _dict):
    for _force in _dict:
        if _user in _dict[_force]:
            _dict[_force].remove(_user)


command = []
operator = []
force_dict = {}

string = input()

while string != "Lumpawaroo":
    command_split(string, command, operator)
    if operator[0] == "|":
        force = command[0]
        user = command[1]
        if user_exists(user, force_dict) is False:
            if force not in force_dict:
                force_dict[force] = [user]
            else:
                force_dict[force] += [user]
    else:
        user = command[0]
        force = command[1]
        if user_exists(user, force_dict):
            delete_user(user, force, force_dict)
        if force not in force_dict:
            force_dict[force] = [user]
        else:
            force_dict[force] += [user]
        print(f'{user} joins the {force} side!')
    string = input()

for key, value in force_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for item in range(len(value)):
            print(f'! {value[item]}')
