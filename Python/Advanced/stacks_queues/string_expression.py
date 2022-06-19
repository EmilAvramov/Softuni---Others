from collections import deque
import operator
from math import floor


def multiply(a, b):
    if a < 0 and b < 0:
        return operator.mul(a, b)
    elif (a > 0 and b < 0) or (a < 0 and b > 0):
        return -operator.mul(a, b)
    else:
        return operator.mul(a, b)


def divide(a, b):
    return floor(operator.truediv(a, b))


def add(a, b):
    return operator.add(a, b)


def sub(a, b):
    return operator.sub(a, b)


data = input().split(" ")
sequence = deque()
result = "start"

for item in data:
    if item != "*" and item != "/" and item != "-" and item != "+":
        if "-" in item:
            sequence.append(-int(item))
        else:
            sequence.append(int(item))
    else:
        sequence.reverse()
        while sequence:
            for number in sequence:
                if item == "*":
                    if result != "start":
                        result = multiply(result, sequence.pop())
                    else:
                        result = sequence.pop()
                    break
                elif item == "/":
                    if result != "start":
                        result = divide(result, sequence.pop())
                    else:
                        result = sequence.pop()
                    break
                elif item == "+":
                    if result != "start":
                        result = add(result, sequence.pop())
                    else:
                        result = sequence.pop()
                    break
                else:
                    if result != "start":
                        result = sub(result, sequence.pop())
                    else:
                        result = sequence.pop()
                    break

print(result)
