def concatenate(*args, **kwargs):
    args = "".join(args)
    for (key, value) in kwargs.items():
        if key in args:
            args = args.replace(key, value)
    return args


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Python"))
