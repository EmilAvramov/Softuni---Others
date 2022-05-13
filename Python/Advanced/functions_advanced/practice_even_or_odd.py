def even_odd(*args):
    args = list(args)
    if args[-1] == "even":
        args.pop()
        return [int(i) for i in args if i % 2 == 0]
    elif args[-1] == "odd":
        args.pop()
        return [int(i) for i in args if i % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
