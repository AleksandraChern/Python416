

from math import pi

area = {
    'Circle': lambda x: pi * x * x,
    'Restangle': lambda x, y: x * y,
    'Trapezoid': lambda a, b, h: (a + b) * h / 2
}


print("Площадь окружности радиуса 2: ", end="")
print(area['Circle'](2))
print("Площадь прямоугольника размером 10 * 13: ", end="")
print(area['Restangle'](10, 13))
print("Площадь трапеции для a=7, b=5, h=3: ", end="")
print(area['Trapezoid'](7, 5, 3))