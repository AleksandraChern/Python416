
#1
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
# print("Тестовые значения: \n2, 4, 6,\n5, 8, 2,\n1, 6, 8\n")
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

#2
#
# s = 0
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
# print("Тестовые значения: \n2, 4, 6,\n5, 8, 2,\n1, 6, 8\n")
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


#3


def outer(a, b, c):
    s = 0

    def inner(i, j):
        nonlocal s
        s += i * j

    inner(a, b)
    inner(a, c)
    inner(b, c)

    return 2 * s

print("Тестовые значения: \n2, 4, 6,\n5, 8, 2,\n1, 6, 8\n")
print(outer(2, 4, 6))
print(outer(5, 8, 2))
print(outer(1, 6, 8))
