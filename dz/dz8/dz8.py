
# import math
# Вычисление площади фигур
from math import sqrt, pi


shape = int(input("Введите фигуры:\n1-треугольник\n2-прямоугольник\n3-круг\n: "))

s = None
if shape == 1:
    a = int(input("Введите сторону a = "))
    b = int(input("Введите сторону b = "))
    c = int(input("Введите сторону c = "))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
elif shape == 2:
    a = int(input("Введите сторону a = "))
    b = int(input("Введите сторону b = "))
    s = a * b
elif shape == 3:
    radius = int(input("Введите радиус = "))
    s = pi * radius ** 2
else:
    print("Такой фигуры не существует")

print(round(s, 2))
