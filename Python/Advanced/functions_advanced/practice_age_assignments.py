def age_assignment(*args, **kwargs):
    names = args
    ages = kwargs
    combined = {}
    for key, value in ages.items():
        for name in names:
            if name[0] == key:
                combined[name] = value

    combined = dict(sorted(combined.items(), key=lambda x: x[0]))
    return "\n".join(
        f"{key} is {value} years old." for key, value in combined.items()
    )


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
