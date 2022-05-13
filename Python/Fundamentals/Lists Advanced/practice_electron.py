number_electrons = int(input())

# Method 1, list generation via electrons, bad, inefficient
# shell_container = [0] * number_electrons
# while number_electrons != 0:
#     for i in range(1, len(shell_container) + 1):
#         if number_electrons >= 2 * (i ** 2):
#             shell_container[i] = 2 * (i ** 2)
#             number_electrons -= 2 * (i ** 2)
#         else:
#             shell_container[i] = number_electrons
#             number_electrons = 0
#             break
#
# shell_container_filtered = list(filter(lambda x: x != 0, shell_container))
# print(shell_container_filtered)

# Method 2, smoother and more efficient method
shell_containers = []
i = 0

while number_electrons != 0:
    i += 1
    shell = 2 * (i ** 2)
    if number_electrons >= shell:
        shell_containers.append(shell)
        number_electrons -= shell
    else:
        shell_containers.append(number_electrons)
        number_electrons = 0

print(shell_containers)


