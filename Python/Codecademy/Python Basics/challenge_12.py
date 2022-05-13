# Task 1
def word_length_dictionary(words):
    result = {}
    for word in words:
        result.update({word : len(word)})
    return result

# Task 2
def frequency_dictionary(words):
    result = {}
    for word in words:
        result.update({word : words.count(word)})
    return result

# Task 3
def unique_values(my_dictionary):
    seen_values = []
    for key, value in my_dictionary.items():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)

# Task 4
def count_first_letter(names):
    result = {}
    for key, value in names.items():
        if key[0] in result:
            result[key[0]] += len(value)
        else:
            result.update({key[0]: len(value)})
    return result
