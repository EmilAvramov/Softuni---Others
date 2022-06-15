from collections import deque


def check(text):
    open_ = tuple("({[")
    close_ = tuple(")}]")
    combined = dict(zip(open_, close_))
    queue = deque()

    for symbol in text:
        if symbol in open_:
            queue.append(combined[symbol])
        elif symbol in close_:
            if not queue or symbol != queue.pop():
                return "NO"
    if not queue:
        return "YES"
    else:
        return "NO"


string = input()
print(check(string))
