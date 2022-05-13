def operate(_operator: str, *args):
    numbers = [int(i) for i in args]
    result = 0
    if _operator == "+":
        result = sum(numbers)
        return result
    elif _operator == "-":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]
        return result
    elif _operator == "*":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result *= numbers[i]
        return result
    else:
        if 0 in numbers:
            return "nan"
        else:
            result = numbers[0]
            for i in range(1, len(numbers)):
                result /= numbers[i]
            return result
