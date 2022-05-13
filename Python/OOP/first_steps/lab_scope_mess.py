# def outer():
#     var = "local"
#     return var


# def outer2():
#     var = "local"

#     def inner():
#         nonlocal var
#         var = "nonlocal"
#         return var

#     return var


# def outer3():
#     var = "local"

#     def inner():
#         nonlocal var
#         var = "nonlocal rebel"
#         return var

#     var = "nonlocal"
#     return var


print("global")
print("outer: local")
print("inner: nonlocal")
print("outer: nonlocal")
print("global: changed!")
