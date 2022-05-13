number = int(input())


def loading_bar():
    if number > 0:
        progress = number // 10
    else:
        progress = 0
    if progress != 10:
        return f'{progress * 10}% [{progress * "%"}{(10 - progress) * "."}] \nStill loading...'
    else:
        return f"100% Complete! \n[{progress * '%'}]"


print(loading_bar())
