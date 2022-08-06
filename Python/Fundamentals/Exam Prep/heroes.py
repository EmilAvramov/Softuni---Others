num_heroes = int(input())
heroes = {}

for i in range(num_heroes):
    [name, hp, mp] = input().split(" ")
    heroes[name] = [int(hp), int(mp)]

command = input()

while command != "End":
    if "CastSpell" in command:
        [cmd, name, mp_needed, spell_name] = command.split(" - ")
        if heroes[name][1] >= int(mp_needed):
            heroes[name][1] -= int(mp_needed)
            print(
                f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!"
            )
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif "TakeDamage" in command:
        [cmd, name, damage, attacker] = command.split(" - ")
        heroes[name][0] -= int(damage)
        if heroes[name][0] > 0:
            print(
                f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!"
            )
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
    elif "Recharge" in command:
        [cmd, name, amount] = command.split(" - ")
        if heroes[name][1] + int(amount) > 200:
            restored = 200 - heroes[name][1]
            print(f"{name} recharged for {restored} MP!")
            heroes[name][1] = 200
        else:
            print(f"{name} recharged for {int(amount)} MP!")
            heroes[name][1] += int(amount)
    elif "Heal" in command:
        [cmd, name, amount] = command.split(" - ")
        if heroes[name][0] + int(amount) > 100:
            restored = 100 - heroes[name][0]
            print(f"{name} healed for {restored} HP!")
            heroes[name][0] = 100
        else:
            print(f"{name} healed for {int(amount)} HP!")
            heroes[name][0] += int(amount)
    command = input()

for [key, value] in heroes.items():
    print(f"{key}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
