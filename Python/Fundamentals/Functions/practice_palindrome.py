numbers = str(input()).split(", ")


def palindrome_function(arguments):
    results = []
    for stream in arguments:
        if stream == stream[::-1]:
            results.append("True")
        else:
            results.append("False")
    return results


print(*palindrome_function(numbers), sep='\n')
