# # # name = "admin"# переменная(комментарий)
# # # # print("Hello," + name+ "!")
# # # age = 20
# # # print(age)
# # # # print(name + str(age))
# # # age = 15.5
# # # print(age)
# # # print(type(name))
# # # print(type(age))
# # # from pickletools import string1
# # #
# # # from pyexpat.errors import messages
# # #
# # # # a = 4
# # # # b = 5
# # # # print(id(a))
# # # # print(id(b))
# # # # a = b # 5
# # # # print(a)
# # # # print(b)
# # # # print(id(a))
# # # # print(id(b))
# # #
# # # # a = b = c = 1
# # # # print(a)
# # # # print(b)
# # # # print(c)
# # #
# # # # a,b,c = 5, "Hello", 9.2
# # # # print(a)
# # # # print(b)
# # # # print(c)
# # # # import keyword
# # # # print(keyword.kwlist)
# # #
# # # # name = "Никита"
# # # # age = 25
# # # # print("Меня зовут " , name, ". Мне", str(age), "лет.")
# # # # первый способ
# # # # a = 10
# # # # b = 2
# # # # print("a:", a)
# # # # print("b:", b)
# # # # c = a
# # # # a = b
# # # # b = c
# # #
# # # # print("a:", a)
# # # # print("b:", b)
# # # # второй способ
# # # # a, b = b, a
# # # # третий способ
# # # # a = 1
# # # # b = 2
# # # # print("a:", a)
# # # # print("b:", b)
# # # # первый способ#
# # # # c = a
# # # # 1# a = b
# # # # 2# b = c
# # # # 1# второй способ#
# # # # a, b = b, a
# # # # третий способa = a + b
# # # # 1 + 2 = 3b = a - b  #
# # # # 3 - 2 = 1a = a - b  # 3 - 1 = 2
# # # # print("a:", a)
# # # # print("b:", b)
# # # # print("строка \
# # # #       символов")
# # # # print('строка\
# # # #       символов')
# # # # print("Документ \"file.txt\" находится по пути: D\\folder\\file.txt")
# # #
# # # # s1 = "Hello"
# # # # s2 = "Python"
# # # # s3 = s1 + " " + s2 + "___"
# # # # print(s3 * 3)
# # #
# # # # print(6 + 2)
# # # # print(6 - 2)
# # # # print(6 * 2)
# # # # print(6 / 2)
# # # # print(7 // 2) #при делении отбросил дробную часть
# # # # print(7 ** 2) #это возведении в степень
# # # # print(7 % 2) #это остаток от деления
# # # #
# # # # a = 5
# # # # b = 7
# # # # c = 3
# # # # print(a + b + c)
# # # # print(a * b * c)
# # # # print((a + b + c)/3) #вывести среднее арифметическое. Это в скобках плюсовать и потом умножить
# # #
# # # # print(6 + 4 * 5 ** 2 + 7) #113 считается слева направо
# # # # print((6 + 4) * (5 ** 2 + 7))#320
# # #
# # # # #операторы присваивания
# # # # num = 10
# # # # num += 5 #num = num + 5 = 15
# # # # print(num)
# # # #
# # # # num -= 3
# # # # print(num)#num = num - 3 = 12
# # # #
# # # # num *= 4
# # # # print(num) #48
# # # #
# # # # #возведение в степень
# # # # num **= 2 # num = num ** 2
# # # # print(num)
# # #
# # # # num = 4321# Исходное число
# # # # print("Исходное число:", num)
# # # # a = num % 10 # это мы находили последнюю цифру
# # # # print("a:", a)
# # # # num = num // 10
# # # # # print(num)
# # # # b = num % 10 # это мы убрали  последнюю цифру 1
# # # # print("b:", b)
# # # # num = num // 10
# # # # # print(num)
# # # # c = num % 10 # это мы убрали  последнюю цифру 2
# # # # print("c:", c)
# # # # num = num // 10
# # # # # print(num)
# # # # d = num % 10 # это мы убрали последнюю цифру 3
# # # # print("d:", d)
# # # # # мы получаем цифры в обратном порядке. нам нужно было 4321 перевернуть в обратном порядке
# # # # print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)
# # #
# # # #
# # # # num = 9753 # 4321
# # # # print("Исходное число:", num)
# # # # res = num % 10 * 1000 # 1000
# # # # num //= 10 # 432
# # # # res += num % 10 * 100 # 200
# # # # # print("Обратное число:", res)
# # # # num //= 10 #43
# # # # res += num % 10 * 10 # 30
# # # # # print("Обратное число:", res)
# # # # num //= 10
# # # # res += num % 10 # 4
# # # # print("Обратное число:", res)
# # #
# # # # num1 = "2"
# # # # num2 = 3
# # # # # res = int(num1) + num2
# # # # res = num1 + str(num2)
# # # # print(res) # 23
# # #
# # # # print(3.8) # есть вещественное число
# # # # print(int(3.8)) # округление данного числа
# # # # print(round(3.8))
# # # # print(type(round(3.8)))
# # # # print(round(3.891)) # это округление данного числа
# # # # print(round(3.895, 2))
# # # # print(type(round(3.899, 2)
# # #
# # # # a = '5.2'
# # # # b = 10
# # # # c = float(a) + b
# # # # print(c)
# # #
# # # # name = "Виктор"
# # # # age = 28
# # # # print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end=" ")
# # # # print("Новая строка")
# # #
# # # # name = input("Введите имя:")
# # # # print("Ваше имя:", name)
# # #
# # # # num = int(input("Введите число: "))
# # # # power = int(input("Введите степень: "))
# # # # res = num ** power
# # # # print ("Число", num, "в степень" , power, "равно", res)
# # #
# # # # num1 = int(input("Введите первое число: "))
# # # # num2 = int(input("Введите второе число: "))
# # # # num3 = int(input("Введите третье число: "))
# # # # num4 = int(input("Введите четвертое число: "))
# # # # sum1 = num1 + num2
# # # # sum2 = num3 + num4
# # # # num1 = int(input("Введите первое число: "))
# # # # num2 = int(input("Введите второе число: "))
# # # # num3 = int(input("Введите третье число: "))
# # # # num4 = int(input("Введите четвертое число: "))
# # # # sum1 = num1 + num2
# # # # sum2 = num3 + num4
# # # # res = sum1 / sum2
# # # # print("Результат = ", round(res,2))
# # # #
# # # #
# # # # b1 = True
# # # # b2 = False
# # # # print(type(b1))
# # # # print(b1 + 5)
# # # # print(b2 + 5)
# # # #
# # # # b1 = True
# # # # b2 = False
# # # # print(type(b1))
# # # # print(b1 + 5)
# # # # print(b2 + 5)
# # # #
# # # # print(bool("python"))
# # # # print(bool(""))
# # # # print(bool(" "))
# # # # print(bool(5))
# # # # print(bool(0))
# # # # print(bool(0.1))
# # # # print(bool(0.0))
# # # # print(bool(False))
# # # # print(bool(None))
# # # # a = Noneprint(a)
# # # # print(type(a))
# # #
# # # # print(7 == 7)
# # # # print(2 + 5 == 7 / 3)
# # # # print(2 + 5 != 7 / 3)
# # # # print(8 > 5)
# # # # print(8 > 8)
# # # # print(8 >= 8)
# # # # print(9 > 9)
# # # # print(9 >= 9)
# # # # print("python" > "Python")  # 112 > 80
# # #
# # # # print(2 < 4 < 9) # True.. True => True
# # # # print(2 * 5 > 7 >= 4 + 3) # 10 > 7 >= 7 true ...True => True
# # # # print(3 * 3 <= 7 >= 2)# 9 <= 7 >= 2 False ...True =>
# # # #
# # # # a = "10"
# # # # b = 10
# # # # c = a == b
# # # # print(a,b,c)
# # #
# # # # print(5 - 3 == 2 and 1 + 3 == 4)  # True and  True => True
# # # # print(5 - 3 == 2 and 1 + 3 < 4)  # True and  False => False
# # # #
# # # # print(5 - 3 == 2 or 1 + 3 == 4)  # True or True => True
# # # # print(5 - 3 == 2 or 1 + 3 < 4)  # True or False => True not(как ! знак)
# # # #
# # # # print(not 9 - 5)
# # # # print(not 7 - 7)
# # # #
# # # # a = 5
# # # # print("a:", a)
# # #
# # # # print("строка текста строка текста строка текста строка текста строка текста строка текста строка текста"
# # # #       " строка текста")
# # #
# # # # cnt = 5
# # # # if cnt < 10:
# # # #     # cnt = cnt + 1
# # # #     cnt += 1
# # # #     print(cnt)
# # #
# # # # age = int(input("Введите свой возраст:"))
# # # # if age >= 18:  # "20" >= 18
# # # #     print("Доступ на сайт разрешен")
# # # # else:
# # # #     print("Доступ запрещён")
# # # #
# # #
# # # # a = 15
# # # # b = 25
# # # # if a > b:
# # # #     print("a > b")
# # # # elif a == b:
# # # #     print("a == b")
# # # # else:
# # # #     print("b > a")
# # #
# # # # a = input("Введите первую строку:")
# # # # b = input("Введите вторую строку:")
# # # # c = input("Введите третью строку:")
# # # #
# # # # if a == b == c: # '10' == '10' == '10'
# # # #     print("Треугольник равносторонний")
# # # # elif a == b or b == c or a == c:
# # # #     print("Треугольник равнобедренный")
# # # # else:
# # # #    print("Треугольник разносторонний")
# # #
# # # # day = int(input("Введите день недели (цифрой):"))
# # # # if 1 <= day <= 5:  # (day >=1) and (day <= 5): # 1 <= 4 <= 5
# # # #     print("Рабочий день - ", end="")
# # # #     if day == 1:
# # # #         print("Понедельник")
# # # #     if day == 2:
# # # #         print("Вторник")
# # # #     if day == 3:
# # # #         print("среда")
# # # #     if day == 4:
# # # #         print("четверг")
# # # #     if day == 5:
# # # #         print("пятница")
# # # # elif day == 6 or day == 7:
# # # #     print("Выходной день - ", end="")
# # # #     if day == 6:
# # # #         print("суббота")
# # # #     if day == 7:
# # # #         print("воскресенье")
# # # # else:
# # # #     print("Такого дня недели не существует")
# # #
# # # # season = int(input("Введите номер месяца: "))
# # # # if 1 <= season <= 12:
# # # #     print("Время года: ", end="")
# # # #     if 1 <= season <= 2 or season == 12:
# # # #         print("Зима")
# # # #     if 3 <= season <= 5:
# # # #         print("Весна")
# # # #     if 6 <= season <= 8:
# # # #         print("Лето")
# # # #     if 9 <= season <= 11:
# # # #         print("Осень")
# # # # else:
# # # #     print("Такого месяца нет")
# # #
# # # # season = int(input("Введите номер месяца: "))
# # # # if 1 <= season <= 2 or season == 12:
# # # #     print("Зима")
# # # #     elif 3 <= season <= 5:
# # # #     print("Весна")
# # # #     elif 6 <= season <= 8:
# # # #     print("Лето")
# # # #     elif 9 <= season <= 11:    (
# # # #         print("Осень"))
# # # # else:
# # # #     print("Такого месяца нет")
# # #
# # # # month = int(input("Введите номер месяца цифрой: "))
# # # # if 12 <= month <= 2:
# # # #     print("Время года - Зима")
# # # #     elif 3 <= month <= 5:
# # # #     print("Время года - Весна")
# # # #     elif 6 <= month <= 8:
# # # #     print("Время года - Лето")
# # # #     elif 9 <= month <= 11:
# # # #     print("Время года - Осень")
# # # # else:
# # # #     print("Некорректное значение")
# # #
# # # # n = int(input("Введите количество ворон:"))
# # # # if 0 <= n <= 9:
# # # #     print("На ветке", end="")
# # # #     if n == 1:
# # # #         print(n, "ворона")
# # # # if 2<= n <=4:
# # # #     print(n, "вороны")
# # # #     if 5<= n <= 9 or n == 0:
# # # #         print(n, "ворон")
# # # #     print("Ошибка ввода")
# # #
# # # # # n = int(input("Введите количество ворон: "))
# # # # if 0 <= n <= 9:
# # # #     print("На ветке ворон", end="")
# # # #     if n == 1:
# # # #         print("а", n)
# # # #     if 2 <= n <= 4:
# # # #         print("ы", n)
# # # #     if 5 <= n <= 9 or n == 0:
# # # #         print("", n)
# # # # else:
# # # #     print("Ошибка ввода")
# # #
# # # # match Выражение:
# # # #     case шаблон_1:
# # # #         действие_1:
# # # #     case шаблон_2:
# # # #         действие_2:
# # #
# # # # password = "user"
# # # #
# # # # match password:
# # # #     case "admin":
# # # #         print("Администратор")
# # # #     case "user":
# # # #         print("Пользователь")
# # # #     case _:
# # # #         print("Пароль неверен")
# # # #
# # # # day = 'понедельник'
# # # # time = 13
# # # #
# # # # match day:
# # # #     case 'понедельник' | 'вторник' | 'среда'| 'четверг' |'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
# # # #         print("Рабочий день")
# # # #     case 'суббота ' | 'воскресенье':
# # # #         print("Выходной день")
# # # #     case _:
# # # #         print("Такого дня не существует или не рабочее время ")
# # #
# # # # day = 'понедельник'
# # # #
# # # # match day:
# # # #     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница':
# # # #    print("Рабочий день")
# # # #     case 'суббота' | 'воскресенье':
# # # #  print("Выходной день")
# # # #      case_:
# # # #     print("Такого дня недели не существует")
# # #
# # # # day = 'понедельник'
# # # # time = 15
# # # # match day:
# # # # case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
# # # #     print("Рабочий день")
# # # #     ase 'суббота' | 'воскресенье':
# # # #     print("Выходной день")
# # # #     case _:        (
# # # #         print("Такого дня недели не существует или нерабочее время"))
# # #
# # # # Тернарное выражение
# # #
# # # # a, b = 30, 20
# # # # print(a if a < b else b)
# # #
# # #
# # # # a, b = 30, 20
# # # # print("На 0 делить нельзя" if b == 0 else a / b)
# # #
# # # # try: # попытаться
# # # #     n = int(input("Введите целое число:"))
# # # #     print(n * 2)
# # # # except ValueError:
# # # #     print("Что-то пошло не так")
# # #
# # # # try: # попытаться
# # # #     n = int(input("Введите делимое:"))
# # # #     m = int(input("Введите делитель:"))
# # # #     print(n / m)
# # # # except ValueError:
# # # #     print("Нельзя вводить строки")
# # # # except ZeroDivisionError:
# # # #         print("Нельзя делить на 0"))
# # #
# # # # try:  # попытаться
# # # #     n = int(input("Введите делимое:"))
# # # #     m = int(input("Введите делитель:"))
# # # #     print(n / m)
# # # # except (ValueError, ZeroDivisionError):
# # # #     print("Нельзя вводить строки или нельзя делить на 0")
# # # # else:  # когда в блоку try не возникло исключениу
# # # #     print("Все нормально. Вы ввели", n, "и", m)
# # # # finally: # выполнится в любом случае
# # # #     print("Конец программы")
# # #
# # #
# # # # try:
# # # #     n = input("Введите первое число:")
# # # #     m = input("Введите второе число:")
# # # #     print(n + m)
# # # # except ValueError:
# # # #     print(str(n) + str(m))
# # #
# # # #
# # # # Циклы
# # # # while условие:
# # # #     блок_когда
# # #
# # # # итерация - один шаг цикла
# # #
# # # # i = 10
# # # # while i > 0:
# # # #     print("i =", i)
# # # #     i += 1
# # #
# # # # i = 1
# # # # while i <= 20:
# # # #     if i % 2 == 0:
# # # #     print(i, end=" ")
# # # #     i += 1
# # #
# # # # print()
# # # # j = 2
# # # # while j <= 20:
# # # #     print(j, end=" ")
# # # #     j += 2
# # #
# # #
# # # # n = int(input("Укажите количество символов: "))
# # # # i = 0
# # # # while i <= n:
# # # #     print("*", end="")
# # # #     i += 1
# # #
# # # # n = int(input("Укажите количество символов: "))
# # # # # print("*" * n)
# # # # while n > 0:
# # # #     print("*", end="")
# # # #     n -= 1
# # #
# # # # a = int(input("Введите начало диапазона:"))
# # # # b = int(input("Введите конец диапазона:"))
# # # # res = 0
# # # # while a <= b: # 1 3 5
# # # #     if a % 2:
# # # #         print(a)
# # # #         res += a
# # # #     a += 1
# # # # print("Сумма нечетных чисел:", res)
# # # #
# # # # n = input("Введите целое число:")
# # # #
# # # # while type(n) != int:  # is not
# # # #     try:
# # # #         n = int(n) # 4
# # # #     except ValueError:
# # # #         print("Число не целое!")
# # # #         n = input("Введите целое число:")
# # # #
# # # # if n % 2 == 0:
# # # #     print("Чётное")
# # # # else:
# # # #     print("Нечётное")
# # #
# # # #
# # # # i = 0
# # # # while i < 10:
# # # #     if i == 3:
# # # #         i += 1
# # # #         continue
# # # #     print(i, end=" ")
# # # #     if i == 5:
# # # #         break
# # # #     i += 1
# # # # print("\n Цикл завершен")
# # #
# # # # i = 0
# # # # while True:
# # # #     print(i)
# # # #     if i == 5:
# # # #         break
# # # #     i += 1
# # #
# # # # while True:
# # # #     n = int(input("Введите положительное число:"))
# # # #     if n < 0:
# # # #         break
# # #
# # #
# # # # while True:
# # # #     n = int(input("Введите число: "))
# # # #     if n == 0:
# # # #         break
# # # # res += print("Произведение чисел: ", res)
# # # #
# # #
# # #
# # # # res = 1
# # # # while True:
# # # #     n = int(input("введите  число: "))
# # # #     if n == 0:
# # # #         break
# # # #         res *= n # res = n * res
# # # # print(res)
# # # #
# # # #
# # # # i = 0
# # # # while i < 10:
# # # #     if i == 5:
# # # #         break
# # # #     print(i)
# # # #     i += 1
# # # # else:
# # # #
# # # # i = 0
# # # # # while i < 10:#
# # # # if i == 5:
# # # #     break
# # # # print(i)
# # # # i += 1  # else:#
# # # # print("Цикл окончен,i = ", i)
# # # #
# # # # # i = 0# while i < 10:#
# # # # if i == 5:  #
# # # #     break  #
# # # # print(i)  #
# # # # i += 1  # print("Цикл окончен, i =", i)
# # #
# # #
# # # # i = 1
# # # # while i < 5:
# # # #     print("Внешний цикл: i =", i)
# # # #     j = 1
# # # #     while j < 4:
# # # #         print("\tВнутренний цикл: j =", j)
# # # #         j += 1
# # # #     i += 1
# # # #
# # #
# # # # while t != "0" and t != "1":
# # # #     t = input("Укажите Ваш выбор числом 0 или 1: ")
# # # #     while n > 0:
# # # #         if t == "0":
# # # #     print(sim, end=" ")
# # # #     else:
# # # #     print(sim)    n -= 1
# # #
# # # # count = input("Укажите кол-во символов: ")
# # # # while type(count) is not int:
# # # #     try:
# # # #         count = int(count)
# # # #         except ValueError:
# # # #         print("Введите целое число")
# # # #         count = input("Введите целое число: ")
# # # #         types = input("Укажите Вид символа: ")
# # # #         orient = input("Укажите направление, 0 - по вертикале, 1 -по горизонтали: ")
# # # #         i = 0
# # # #         while i <= count:    if
# # # #         orient == 1: print(types, end=" ")
# # # #         if orient == 0:        print(types, end="\n")
# # # #         i += 1
# # # #         while type(orient) is not int:        i = 0
# # # #         try:            orient = int(orient)
# # # #         if orient == 0 or orient == 1:
# # # #             pass else:
# # # #             print("Неверное направление!")
# # # #         orient = input("Введите направление 1 или 0: ")
# # # # except ValueError: print("Неверное направление!")
# # # # orient = input("Введите направление 1 или 0: ")
# # # # i += 1
# # #
# # # # # range(start, stop,step)
# # # # print(range(1, 10, 2))
# # # #
# # # # for i in range(1, 10, 2):
# # # #     print(i, end=" ")
# # # #
# # # # for i in range(3): # for (let i = 0; i < 3; i++) # i = 0
# # # #     print("+++")
# # # #     for j in range(2): # for(let j = 0; j < 2; j++) # j = 0
# # # #         print("-----")
# # #
# # # # w = 16
# # # # h = 5
# # # # for i in range(h):
# # # #     for j in range(w):
# # # #         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
# # # #             print("*", end="")
# # # #         else:
# # # #             print(" ", end="")
# # # #     print()
# # #
# # #
# # # # w = int(input("Введите ширину прямоугольника: "))
# # # # h = int(input("Введите высоту прямоугольника: "))
# # # # for i in range(h):
# # # #     for j in range(w):
# # # #         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
# # # #             print("* ", end="")
# # # #         else:
# # # #             print("  ", end="")
# # # #     print()
# # #
# # #
# # # # string = [letter * 2 for letter in "Python"]
# # # # print(string)
# # #
# # # # for letter in "Python":
# # # #     print(letter * 2, end="\t")
# # #
# # #
# # # # num = [i for  i in range(30) if i % 2 == 0]
# # # # print(num)
# # # #
# # # # print()
# # # #
# # # # for i in range(30):
# # # #     if i % 2 == 0:
# # # #         print(i, end="\t")
# # #
# # # # num = [8, 3, 9, 4, 1, "one", True]
# # # # print(nums)
# # # # print(nums[0])
# # # # print(nums[-5])
# # # # print(nums[4])
# # # # print(nums[-1])
# # # # print(nums[-2])
# # #
# # # # nums = [8, 3, 9, 4, 1]
# # # # print(nums)
# # # # nums[1] = 256
# # # # print(nums)
# # # # nums[3] += 100
# # # # print(nums)
# # #
# # # # nums = [8, 3, 9, 4, 1]
# # # # print(nums, id(nums))
# # # # print(nums[0], id(nums[0]))
# # # # print(nums[1], id(nums[1]))
# # # # nums[1] = 256
# # # # print(nums[1], id(nums[1]))
# # # # print(nums, id(nums))
# # # # print("Длина списка:", len(nums))
# # # #
# # #
# # # # nums = [8, 3, 9, 4, 1]
# # # # nums2 = [11, 12, 13]
# # # # n = nums + nums2
# # # # print(n)
# # # # print(n * 3)
# # #
# # # # print(list("Hello"))
# # # #
# # # # print(range(10))
# # # # print(list(range(10)))
# # # # print(list(range(2, 10)))
# # # # print(list(range(10, 2, -2)))
# # #
# # # # [выражение for переменная in последовательность]
# # #
# # # # a = [0 for i in range(5)]    # 0 1 2
# # # # print(a) # [0, 0, 0, 0, 0]
# # #
# # # # n = 5
# # # # a = [i ** 2 foe i in range(1, n + 1)]
# # # # print(a) # [1, 4, 9, 16]
# # # #
# # # # a = [0] * int(input("Введите количество элементов списка: "))
# # # # print(a)
# # # # for i in range(len(a)):
# # # #     a[i] = int(input("-> "))
# # # # print(a)
# # #
# # #
# # # # a = [int(input("-> ")) for i in range(int(input("n =")))]
# # # # print(a)
# # #
# # #
# # # # print(list(range(0, -5, -1)))
# # #
# # # # name = ['svetlana', 'nina', 'szabina', 'aleksandr', 'aleksandra']
# # # # print(name)
# # # # name = ['svetlana', 'nina', 'szabina', 'aleksandr', 'aleksandra']
# # # # print(name[0])
# # # # print(name[1])
# # # # print(name[2])
# # # # print(name[3])
# # # # print(name[4])
# # #
# # # #
# # # # motorsicle = ['honda', 'suzuki', 'ural', 'yamaha', 'ducati']
# # # # print(motorsicle)
# # # #
# # # # messages = f"\"Я хотела бы купить мотоцикл {motorsicle[0].title()}.\""
# # # # print(messages)
# # # # messages = f"\" Я люблю кататься  на мотоцикле {motorsicle[1].title()}, на большой скорости \"."
# # # # print(messages)
# # # # messages = f"\" У моего папы был большой мотоцикл, он назывался {motorsicle[2].title()}, она нас часто катал на нём когда мы были маленькими.\""
# # # # print(messages)
# # # # messages = f"\"Отличный мотоцикл {motorsicle[3].title()},у него большая скорость.\""
# # # # print(messages)
# # # # messages = f"\"{motorsicle[4].title()} - это отличный и очень дорогой мотоцикл.\""
# # # # print(messages)
# # # #
# # # # motorsicle = ['honda', 'suzuki', 'ural', 'yamaha']
# # # # print(motorsicle)
# # # #
# # # # # motorsicle[0] = 'dicati'
# # # # # print(motorsicle)
# # # #
# # # # motorsicle.append('ducati')
# # # # print(motorsicle)
# # #
# # # # motorsicle = []
# # # # motorsicle.append('honda') # добавление в список
# # # # motorsicle.append('suzuki')
# # # # motorsicle.append('ural')
# # # # motorsicle.append('ducati')
# # # # print(motorsicle)
# # # #
# # # # motorsicle = ['honda', 'suzuki', 'ural', 'yamaha'] # вставка элементво в список
# # # # motorsicle.insert(1, 'subaru')
# # # # motorsicle.insert(2,'ducati')
# # # # motorsicle.insert(0, 'dacota')
# # # # print(motorsicle)
# # #
# # #
# # # # motorsicle = ['honda', 'suzuki', 'ural', 'yamaha'] # удаление из списка навсегда
# # # # del motorsicle[0]
# # # # del motorsicle[2]
# # # # print(motorsicle)
# # #
# # # # motorsicle = ['honda', 'suzuki', 'ural', 'yamaha'] # это метод удаления и помещение этого значесния в другую переменную и дальнйшее её использования
# # #
# # # # popped_motorsicle = motorsicle.pop()
# # # # print(motorsicle)
# # # # print(popped_motorsicle)
# # #
# # # # last_owen = motorsicle.pop()
# # # # print(f"I liked my last motorsicle was {last_owen.title()}")
# # #
# # # # name = ['nina', 'szabina', 'sveta', 'nastya']
# # #
# # # # name.append('aleksandra') # Это добавление в элемент списка
# # # # name.append('aleksandr')
# # # # name.append('ferenc')
# # # # name.insert(1,'ferenc')
# # # # name.insert(2,'aleksandra')
# # # # name.insert(3,'svetlana')
# # #
# # # # name = ['nina', 'szabina', 'sveta', 'nastya']
# # # # popped_names = name.pop(3)
# # # # print(name)
# # # # print(popped_names)
# # # #
# # # # name = ['nina', 'szabina', 'sveta', 'nastya']
# # # # del name[1]
# # # # print(name)
# # #
# # # # name = ['nina', 'szabina', 'sveta', 'nastya']
# # #
# # # # very_far = 'szabina'
# # # # name.remove('szabina')
# # # # print(name)
# # # # print(f"\"{very_far.title()} живёт очень и очень далеко.\"")
# # # #
# # # # too_much = 'sveta'
# # # # name.remove('sveta')
# # # # print(name)
# # # # print(f"\"{too_much.title()}  очень много работает и очень редко отдыхает\"")
# # #
# # # # name = ['nina', 'ferenc', 'sveta', 'nastya', 'aleksandra']
# # # # print(f"\" Дорогая {name[0].title()} хочу пригласите тебя на обед.\"")
# # # # print(f"\"С удовольствие буду рада видеть тебя {name[1].title()} на обеде\".")
# # # # print(f"\"Желаю тебе выздоровления и после приглашаю тебя дорогая {name[2].title()} на обед, люблю тебя!\"")
# # # # print(f"\"{name[1].title()} не сможет придти, потому что плохо себя ведёт\".")
# # # #
# # # # name[1] = 'alersandr'
# # # # print(name)
# # # # print(f"\" Дорогая {name[0].title()} хочу пригласите тебя на обед, желаю тебе чтобы операция прошла успешно.\"")
# # # # print(f"\"Дорогой {name[1].title()} буду очень рада тебя видеть у нас на обеде.\"")
# # # # print(f"\"Дорогая сестричка {name[2].title()} очень жду встречи с тобой и приглашаю тебя к нам на обед.\"")
# # # #
# # # #
# # # #
# # # # a = [1, 2, 3, 55, 66]b = [11, 22, 33]c = []if len(a) > len(b):
# # # # a, b = b, afor i in range(len(a)):  # 0 1 2    c.append(a[i])
# # # #     # c.append(b[i])for i in range(len(a), len(b)):
# # # #     # range(3, 5):
# # # #     # c.append(b[i])# if len(b) > len(a):#
# # # #     # for i in range(len(a)):  # 0 1 2#
# # # #     # c.append(a[i])#         c.append(b[i])#
# # # #     # for i in range(len(a), len(b)):
# # # #     # range(3, 5):#
# # # #     # c.append(b[i])# else:#
# # # #     # for i in range(len(b)):  # 0 1 2#
# # # #     # c.append(a[i])#         c.append(b[i])#
# # # #     # for i in range(len(b), len(a)):  # range(3, 5):#
# # # # #     c.append(a[i])print(c)  # [1, 11, 2, 22, 3, 33, 4, 2]
# # # #
# # # # a = [1, 2, 3, 55, 66]b = [11, 22, 33]c = []if len(a) > len(b):
# # # #     a, b = b, afor i in range(len(a)):  # 0 1 2
# # # #     #  c.append(a[i])    c.append(b[i])for i in range(len(a), len(b)):  # range(3, 5):
# # # #     #  c.append(b[i])# if len(b) > len(a):#     for i in range(len(a)):  # 0 1 2#
# # # #     #  c.append(a[i])#         c.append(b[i])#     for i in range(len(a), len(b)):  # range(3, 5):#
# # # #     #  c.append(b[i])# else:#     for i in range(len(b)):  # 0 1 2#         c.append(a[i])#
# # # #     #  c.append(b[i])#
# # # # # for i in range(len(b), len(a)):  # range(3, 5):#
# # # # # c.append(a[i])print(c)  # [1, 11, 2, 22, 3, 33, 4, 2]
# # # # #
# # # # # a = [int(input("-> ")) for i in range(int(input("n = ")))]
# # # # #
# # # # #
# # # # # city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # # # #
# # # # # city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # # # #
# # # # # s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# # # # #
# # # # # city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # # # # s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# # # # # print(random.choice(city_list))print(random.choice(s))
# # # # # print(random.choices(city_list, k=3))
# # # # # print(random.choices(s, k=3))
# # # # #
# # # # # Собрание
# # # # # запланировано
# # # # # 16: 12 Meeting
# # # # # ended: 16
# # # # # s
# # # # #
# # # # # 16: 14 Meeting
# # # # # started
# # # # #
# # # # # lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# # # # # new_lst = []
# # # # # i = 0
# # # # # for element in lst:    k = element
# # # # # for element in lst:        if
# # # # # k == element: i += 1
# # # # # if i == 1:        print(k, end=" ")
# # # # # new_lst.append(k)
# # # # # i = 0
# # # # #
# # # # # добрый
# # # # # вечер, немного
# # # # # опоздала, отметьте
# # # # # пожалуйста
# # # # #
# # # # # a = [1, 2, 3, 55, 66]
# # # # # b = [11, 22, 33]
# # # # # c = []
# # # # # if len(a) > len(b):    a, b = b, afor
# # # # # i in range(
# # # # #     len(a)):  # 0 1 2    c.append(a[i])    c.append(b[i])for i in range(len(a), len(b)):  # range(3, 5):    c.append(b[i])# if len(b) > len(a):#     for i in range(len(a)):  # 0 1 2#         c.append(a[i])#         c.append(b[i])#     for i in range(len(a), len(b)):  # range(3, 5):#         c.append(b[i])# else:#     for i in range(len(b)):  # 0 1 2#         c.append(a[i])#         c.append(b[i])#     for i in range(len(b), len(a)):  # range(3, 5):#         c.append(a[i])print(c)  # [1, 11, 2, 22, 3, 33, 4, 2]
# # # # #
# # # # # а
# # # # # переменка ?
# # # # #
# # # # # a = [int(input("-> ")) for i in range(int(input("n = ")))]
# # # # #
# # # # # city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # # # #
# # # # # s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# # # # #
# # # # # city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # # # # s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# # # # # print(random.choice(city_list))
# # # # # print(random.choice(s))
# # # # # print(random.choices(city_list, k=3))
# # # # # print(random.choices(s, k=3))
# # # # #
# # # # #
# # # # #
# # # # # city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # # # # s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
# # # # # print(random.choice(city_list))
# # # # # print(random.choice(s))
# # # # # print(random.choices(city_list, k=3))
# # # # # print(random.choices(s, k=3))
# # # # #
# # # # #
# # # # # import randommas = [random.randint(0, 100) for i in range(10)]print(mas)
# # # # #
# # # # #
# # # # #
# # # # # lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# # # # # new_lst = []i = 0
# # # # # for element in lst:
# # # # #     k = element
# # # # #     for element in lst:
# # # # #         if k == element:
# # # # #             i += 1
# # # # #             if i == 1:
# # # # #                 print(k, end=" ")
# # # # #                 new_lst.append(k)
# # # # #                 i = 0
# # # # #
# # # # # lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# # # # # new_lst = []i = 0
# # # # # for element in lst:
# # # # #     k = element
# # # # #     for element in lst:
# # # # #     if k == element:
# # # # #         i += 1
# # # # #         if i == 1:
# # # # #             print(k, end=" ")
# # # # #             new_lst.append(k)
# # # # #             i = 0
# # # #
# # # #
# # # # # res = time.localtime()print(res.tm_year, "-0", res.tm_mon, "-0", res.tm_mday, sep="")
# # # # # print(time.strftime("Today is %B %d, %Y"))
# # # # #
# # # # #
# # # # # import timestart = time.monotonic()pause = 5print('Программа запущена')
# # # # # time.sleep(pause)result = time.monotonic() - startprint('Программа выполнен за', result, 'секунд')
# # # #
# # # # # Функции# def hello(name, age):#
# # # # # print("Меня зовут " + str(name) + ". Мне " + str(age) + " лет.")
# # # # # hello("Irina", 28)# hello("Ivan", 15)
# # # # #
# # # # # def add(x, y):
# # # # #     if x > y:
# # # # # return x - y
# # # # # else:
# # # # # return x + ya = int(input("a = "))
# # # # # b = int(input("b = "))
# # # # # print(add(a, b))
# # # #
# # # # # def check_password(password):
# # # # #     has_upper = False
# # # # #     has_lower = False
# # # # #     has_num = False
# # # # #     for ch in password:
# # # # #         if "A" <= ch <= "Z":
# # # # #             has_upper = True
# # # # #             if "a" <= ch <= "z":
# # # # #                 has_lower = True
# # # # #                 if "0" <= ch <= "9":
# # # # #                     has_num = True
# # # # #                     if len(password) >= 8 and has_upper and has_lower and has_num:
# # # # #                         return True
# # # # #                         return Falsep = input("Введите пароль: ")
# # # # # if check_password(p):
# # # # #     print("Это надежный пароль")
# # # # # else:    print("Это ненадежный пароль")
# # # # #
# # # # #
# # # # # def get_sum(a, b, c=0, d=1):
# # # # #     return a + b + c + dprint(get_sum(7, 9, d=3, c=5))
# # # # # print(get_sum(1, 5, 2, 7))
# # # # # print(get_sum(1, 5, 2))
# # # # # print(get_sum(1, 5))
# # # # # print(get_sum(1, 5, d=2))
# # # # #
# # # # # def display_info(name, age):
# # # # #     print("Name:", name, "\nAge:", age)
# # # # # display_info("Ira", 23)display_info(23, "Ira")
# # # # # display_info(age=23, name="Ira")
# # # # # display_info("Igor", age=23, name="Ira")
# # # #
# # # #
# # # # name2 = "admin"
# # # # print(name2)
# # # #
# # # # firstName = "admin"
# # # # print(firstName)
# # # #
# # # # first_name = "admin"
# # # # print("first_name")
# # #
# # # # import keyword
# # # # print(keyword.kwlist)
# # #
# # #
# # # # name = "Никита"
# # # # age = 25
# # # # print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# # #
# # #
# # # # a = 1
# # # # b = 2
# # # # print("a:", a)
# # # # print("b:", b)
# # # # c = a
# # # # a = b
# # # # b = c
# # # # print("a:", a)
# # # # print("b:", b)
# # #
# # # # print("Документ \"file.txt\"")
# # # # print(6 + 2)
# # # # print(6 - 2)
# # # # print(6 * 2)
# # # # print(7 / 2)
# # # # print(7 // 2)
# # #
# # # #
# # # # print(6 + 4 * 5 ** 2 + 7) # 113
# # # # print((6 + 4) * (5 ** 2 + 7)) #320
# # #
# # # # num = 10
# # # # num += 5 # 15
# # # # print(num)
# # # #
# # # # num -= 3
# # # # print(num)# 12
# # # #
# # # # num *= 4 # 48
# # # # print(num)
# # # #
# # # # num **= 2 # 2304
# # # # print(num)
# # # #
# # # # num = 4321
# # # # print("Исходное число:", num)
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # # # print(num)
# # # # b = num % 10
# # # # print("b:", b)
# # # # num = num // 10
# # # # # print(num)
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # # # print(num)
# # # # d = num % 10
# # # # print("d:", d)
# # # # print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)
# # #
# # # #
# # # # num = 4321
# # # # print("Исходное число:", num)
# # # # res = num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # print("Обратное число:", res)
# # #
# # #
# # # # #НАписать пятизначное число в обратном порядке
# # # #
# # # # num = 78965
# # # # print("Исходное число:", num)
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # # # print(num)
# # # # b = num % 10
# # # # print("b:", b)
# # # # num = num // 10
# # # # # print(num)
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # # # print(num)
# # # # d = num % 10
# # # # print("d:", d)
# # # # num = num // 10
# # # # e = num % 10
# # # # print("e:", e)
# # # # num = num // 10
# # # # # print(num)
# # # # print("Обратное число:", a * 10000 + b * 1000 + c * 100 + d * 10 + e)
# # #
# # # # НАписать пятизначное число в обратном порядке
# # #
# # # # num = 78965
# # # # print("Исходное число:", num)
# # # # res = num % 10 * 10000
# # # # num //= 10
# # # # res += num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # print("Обратное число:", res)
# # #
# # #
# # # # num = 4321
# # # # print("Исходное число:", num)
# # # # res = num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # print("Обратное число:", res)
# # #
# # # # num = 65789
# # # # print("Исходное число:", num)
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # # print(num)
# # # # b = num % 10
# # # # print("b:", b)
# # # # num = num // 10
# # # # print(num)
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # # print(num)
# # # # d = num % 10
# # # # print("d:", d)
# # # # num = num // 10
# # # # print(num)
# # # # e = num % 10
# # # # print("e:", e)
# # # # num = num // 10
# # # # # print(num)
# # # # print("Конечно число:", a * 10000 + b * 1000 + c * 100 + d * 10 + e )
# # #
# # # # num = 65789
# # # # print("Исходное число:", num)
# # # # res = num % 10 * 10000
# # # # num //= 10
# # # # res += num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # print("Конечное число:", res)
# # #
# # # # num = 123
# # # # print("Исходное число:", num)
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # # print(num)
# # # # b = num % 10
# # # # print("b:",b)
# # # # num = num // 10
# # # # print(num)
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # # print(num)
# # # # print("Конечный результат:", a * 100 + b * 10 + c)
# # #
# # # # num = 123
# # # # print("Исходное число:", num)
# # # # res = num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # print("Конечный результат:", res)
# # #
# # # # num = 1122
# # # # print("Исхлдное число:", num)
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # # print(num)
# # # # b = num % 10
# # # # print("b:", b)
# # # # num = num // 10
# # # # print(num)
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # # print(num)
# # # # e = num % 10
# # # # print("e:", e)
# # # # num = num // 10
# # # # print(num)
# # # # print("Конечный результат:", a % 10 * 1000 + b % 10 * 100 + c % 10 * 10 + e)
# # #
# # # # num1 = "2"
# # # # num2 = 3
# # # # # res = int(num1) + num2
# # # # res = num1 + str(num2)
# # # # print(res) # 5
# # #
# # # #
# # # # def func(a, b=0):
# # # # return a + bprint(func(2, 5))
# # # #
# # # #
# # # # print(func(b=2, a=5))
# # # # print(func(2))
# # # #
# # # # lst1 = [1, 2, 3]# lst2 = [1, 2, 3]#
# # # # print(lst1, id(lst1))#
# # # # print(lst2, id(lst2))#
# # # # print(lst1 == lst2)#
# # # # print(lst1 is lst2)# #
# # # # a = "Hello"# b = "Hello"#
# # # # print(a, id(a))# print(b, id(b))#
# # # # print(a == b)#
# # # # print(a is b)
# # #
# # # # a = "Hello"
# # # # print(a, id(a))
# # # # a = a + "!"
# # # # print(a, id(a))
# # # #
# # # # lst = [10, 20, 30]
# # # # tpl = (10, 20, 30)
# # # # print(lst.__sizeof__())
# # # # print(tpl.__sizeof__())
# # #
# # # # print(t3.count('l'))#
# # # # print(t3.count('a'))## #
# # # # print(t3.index("l", 9))# if 'e' in t3:#
# # # # print(t3.index("e"))# else:#
# # # # print("Такого элемента нет")
# # # #
# # # # def slicer(tpl, el):    ...
# # # #
# # # #
# # # # print(slicer((1, 2, 3), 8))
# # # # print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# # # # print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# # # #
# # # #
# # # # def slicer(tpl, el):    ...
# # # #
# # # #
# # # # print(slicer((1, 2, 3), 8))
# # # # print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# # # # print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# # #
# # # #
# # # # a = "Hello"
# # # # print(a, id(a))
# # # # a = a + "!"
# # # # print(a, id(a))
# # # #
# # # # from random import randintprint
# # # #
# # # # (tuple(i for i in range(10)))
# # # # print(tuple(input("-> ")
# # # #             for i in range(5)))
# # # # print(tuple(randint(50, 100)
# # # #             for i in range(10)))
# # # #
# # # # t1 = tuple("hello")
# # # # t2 = tuple("world")
# # # # t3 = t1 + t2print(t3)
# # # #
# # # #
# # # # # print(t3.count('l'))#
# # # # # print(t3.count('a'))## #
# # # # # print(t3.index("l", 9))# if 'e' in t3:#
# # # # # print(t3.index("e"))# else:#
# # # # # print("Такого элемента нет")
# # # #
# # # # def slicer(tpl, el):    ...
# # # #
# # # #
# # # # print(slicer((1, 2, 3), 8))
# # # # print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# # # # print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# # # #
# # # # countries = (
# # # #     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))), ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),)
# # # # print(countries)
# # # # for country in countries:    country_name, country_population, cities = country
# # # # print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
# # # # for city in cities:        city_name, city_population = city
# # # # print("\tГород: ", city_name, ", население = ",
# # # #       city_population, sep="")
# # # #
# # # # countries = (
# # # #     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))), ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),)
# # # # print(countries)
# # # # for country in countries:    country_name, country_population, cities = country
# # # # print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
# # # # for city in cities:        city_name, city_population = city
# # # # print("\tГород: ", city_name, ", население = ", city_population, sep="")
# # # #
# # # # tpl = tuple(input("Введите строку: "))
# # # # print(tpl)
# # # # lst = []
# # # # for i in range(len(tpl)):    if
# # # # tpl[i] not in lst: lst.append(tpl[i])
# # # # print(lst)
# # # # for i in range(len(lst)):    print("Количество", lst[i], "=", tpl.count(lst[i]))
# # # #
# # # #
# # # # tpl = tuple(input('Введите строку: '))
# # # # print(tpl)
# # # # lst = []
# # # # for i in range(len(tpl)):
# # # #     if tpl[i] not in lst:
# # # #         lst.append(tpl[i])
# # # # print(lst)
# # # # for i in range(len(lst)):
# # # #     print('Количество', lst[i], '=', tpl.count(lst[i]))
# # # #
# # # #
# # # # Напишите число в обратном порядкею
# # #
# # # # num = 9574
# # # # print("Введите число:", num)
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # # print(num)
# # # # b = num % 10
# # # # print("b:", b)
# # # # num = num // 10
# # # # print(num)
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # # print(num)
# # # # d = num % 10
# # # # print("d:", d)
# # # # num = num // 10
# # # # # print(num)
# # # # print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)
# # #
# # # # num = 9574
# # # # print("Введите число:", num)
# # # # res = num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # num //= 10
# # # # print("Обратное число:", res
# # #
# # # #
# # # # num = 8975
# # # # print(num)
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # # b = num % 10
# # # # print("b:", b)
# # # # num = num // 10
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # # d = num % 10
# # # # print("d:", d)
# # # # num = num // 10
# # # # print("Обратная цифра:", a * 1000 + b * 100 + c * 10 + d)
# # # #
# # # # num = 8975
# # # # print("Исходное число", num)
# # # # res = num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # num //= 10
# # # # print("Обратное число:", res)
# # # #
# # # # name = "Виктор"
# # # # age = 25
# # # # print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# # #
# # # # name = input("Ведите имя: ")
# # # # print("Ваше имя:", name)
# # #
# # # #
# # # # num = int(input("Введите число: "))
# # # # power = int(input("Введите в степень: "))
# # # # res = num ** power
# # # # print("Число", num, "в степени", power, "равно:", res)
# # #
# # # #
# # # # num = int(input("Введите четыре числа: "))
# # # # num1 = int(input("1: "))
# # # # num2 = int(input("2: "))
# # # # num3 = int(input("3: "))
# # # # num4 = int(input("4: "))
# # # #
# # # # sum1 = num1 + num2
# # # # sum2 = num3 + num4
# # # # res = sum1 / sum2
# # # # print(round(res, 2))
# # #
# # # # num1 = int(input("Введите первое число:"))
# # # # num2 = int(input("Введите второе число:"))
# # # # num3 = int(input("Введите третье число:"))
# # # # num4 = int(input("Введите четвёртое число:"))
# # # # num5 = int(input("Введите пятое число:"))
# # # #
# # # # print("Введите пятизначное число: 97531")
# # # # print("Произведение цифр числа: ", num1 * num2 * num3 * num4 * num5)
# # # # print("Среднее арифметическое числа: ", (num1 + num2 + num3 + num4 + num5) / 5)
# # #
# # #
# # # #
# # # # cop1 = int(input("Введите первое число: "))
# # # # cop2 = int(input("Введите второе число: "))
# # # # cop3 = int(input("Введите третье число: "))
# # # # cop4 = int(input("Введите четвертое число: "))
# # # #
# # # # sum1 = cop1 + cop2
# # # # sum2 = cop3 + cop4
# # # # res = sum1 / sum2
# # # # print("Результат:", (round(res, 2)))
# # # # # print(round(res, 2))
# # # #
# # #
# # # #
# # # # cop1 = int(input("Введите первое число: "))
# # # # cop2 = int(input("Введите второе число: "))
# # # # cop3 = int(input("Введите третье число: "))
# # # # cop4 = int(input("Введите четвёртое число: "))
# # # # cop5 = int(input("Введите пятое число: "))
# # #
# # #
# # # # num = int(input("Введите пятизначное число:"))
# # # # a = num % 10
# # # # num //= 10
# # # # b = num % 10
# # # # num //= 10
# # # # c = num % 10
# # # # num //= 10
# # # # d = num % 10
# # # # num //= 10
# # # # e = num % 10
# # # # num //= 10
# # # # # print("b:", b)
# # # # # print("e:", e)
# # # # print("Произведение числа:", a * b * c * d * e)
# # # # print("Среднее арифметическое:", (a + b + c + d + e) / 5)
# # #
# # # #
# # # # num = int(input("Введите пятизначное число:"))
# # # # a = num % 10
# # # # num //= 10
# # # # b = num % 10
# # # # num //= 10
# # # # d = num % 10
# # # # num //= 10
# # # # c = num % 10
# # # # num //= 10
# # # # e = num % 10
# # # # num //= 10
# # # #
# # # # print("Произведение цифр чисел:", a * b * c * d * e)
# # # # print("Среднее арифметическое:", (a + b + c + d + e) / 5)
# # #
# # # # res = num % 10 * 10000
# # # # num //= 10
# # # # res += num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # print("Произведение числа:", )
# # #
# # #
# # # # print("Произведение цифр числа:", cop1 * cop2 * cop3 * cop4 * cop5)
# # # # print("Среднее арифметическое:", (cop1 + cop2 + cop3 + cop4 + cop5) / 5)
# # #
# # #
# # # # num = int(input("Исходное число: 9753\n"))
# # # #
# # # # a = num % 10
# # # # print("a:", a)
# # # # num = num // 10
# # # #
# # # # b = num % 10
# # # # print("b:", b)
# # # # num = num // 10
# # # #
# # # # c = num % 10
# # # # print("c:", c)
# # # # num = num // 10
# # # #
# # # # d = num % 10
# # # # print("d:", d)
# # # # num = num // 10
# # # #
# # # # print("Конечное число:", a * 1000 + b * 100 + c * 10 + d)
# # # #
# # #
# # # # num = 5897
# # # # print("Исходное число:", num)
# # # # res = num % 10 * 1000
# # # # num //= 10
# # # # res += num % 10 * 100
# # # # num //= 10
# # # # res += num % 10 * 10
# # # # num //= 10
# # # # res += num % 10
# # # # print("Обратное число:", res)
# # #
# # # # print(5 - 3 == 2 and 1 + 3 == 4)
# # # #
# # # # age = int(input("Введите свой возраст: "))
# # # # if age >= 18:
# # # #     print("Доступ разрешён")
# # # # else:
# # # #     print("Доступ запрещён")
# # # #
# # # # a = 15
# # # # b = 25
# # # # if a > b:
# # # #     print("a > b")
# # # # elif a == b:
# # # #     print("a == b")
# # # # else:
# # # #     print("b > a")
# # # #
# # # # a = int(input("Введите первую строку: "))
# # # # b = int(input("Введите вторую строку: "))
# # # # c = int(input("Введите третью строку: "))
# # # #
# # # # if a == b == c:
# # # #     print("Треугольник равносторонний ")
# # # # elif a == b or b == c or a == c:
# # # #     print("Треугольник равнобедренный ")
# # # # else:
# # # #     print("Треугольник разносторонний ")
# # #
# # #
# # # # day = int(input("Введите дни недели (цифрой): "))
# # # # if 1 <= day <= 5:   # (day >= 1) and (day <= 5):
# # # #     print("Рабочий день - ", end="")
# # # #     if day == 1:
# # # #         print("Понедельник ")
# # # #     if day == 2:
# # # #         print("Вторник")
# # # #     if day == 3:
# # # #         print("Среда")
# # # #     if day == 4:
# # # #         print("Четверг")
# # # #     if day == 5:
# # # #         print("Пятница")
# # # # elif day == 6 or day == 7:
# # # #     print("Выходной день - ", end="")
# # # #     if day == 6:
# # # #         print("Суббота ")
# # # #     if day == 7:
# # # #         print("Воскресенье ")
# # # # else:
# # # #     print("Такого дня не существует ")
# # #
# # #
# # # #
# # # # month = int(input("Введите номер месяца года (цифрой): "))
# # # # if <= 1 or <= 12:
# # # #     print("Время года - ", end=)
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 2:
# # # #         print("Февраль")
# # # #     if month == 1:
# # # #         print("Март")
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 1:
# # # #         print("Январь")
# # # #     if month == 1:
# # # #          print("Январь")
# # # #     if month == 1:
# # # #         print("Январь")
# # # # else:
# # # #     print("Ошибка ввода данных ")
# # # #
# # # #
# # # # time = int(input("Введите номер месяца года (цифрой): "))
# # # # if time <= 1 or time <= 12:
# # # #     if time == 1 or time == 2 or time == 12:
# # # #         print("зима: ", end="")
# # # #         if time == 1:
# # # #             print("январь ")
# # # #         if time == 2:
# # # #             print("февраль")
# # # #         if time == 12:
# # # #             print("декабрь")
# # # #     if 3 <= time <= 5:
# # # #         print("весна: ", end="")
# # # #         if time == 3:
# # # #             print("март")
# # # #         if time == 4:
# # # #             print("апрель")
# # # #         if time == 5:
# # # #             print("май")
# # # #     if 6 <= time <= 8:
# # # #         print("лето: ", end="")
# # # #         if time == 6:
# # # #             print("июнь")
# # # #         if time == 7:
# # # #             print("июль")
# # # #         if time == 8:
# # # #             print("август")
# # # #     if 9 <= time <= 11:
# # # #         print("осень: ", end="")
# # # #         if time == 9:
# # # #             print("сентябрь")
# # # #         if time == 10:
# # # #             print("октябрь")
# # # #         if time == 11:
# # # #             print("ноябрь")
# # # # else:
# # # #     print("Ошибка ввода данных ")
# # #
# # #
# # # # n = int(input("Введите количество ворон: "))
# # # # if 0 <= n <= 9:
# # # #     print("На ветке ворон", end="")
# # # #     if n == 1:
# # # #         print("а", n)
# # # #     if 2 <= n <= 4:
# # # #         print("ы", n)
# # # #     else:                        # if 5 <= n <= 9 or n == 0:
# # # #         print("", n)
# # # # else:
# # # #     print("Ошибка ввода")
# # # #
# # # # a = int(input("Введите количество копеек  от 1 до 99: "))
# # # # cop = a
# # # # if 11 <= cop <= 14:
# # # #     print(a, "копеек")
# # # # elif 1 <= a <= 10 or 15 <= a <= 99:
# # # #     cop = cop % 10
# # # #     if cop == 1:
# # # #         print(a, "копейка")
# # # #     elif 2 <= cop <= 4:
# # # #         print(a, "копейки")
# # # #     else:
# # # #         print(a, "копеек")
# # # # else:
# # # #     print("Значения должны быть от 1 до 99")
# # #
# # # #
# # # # password = "fghgdfg"
# # # #
# # # # match password:
# # # #     case "admin":
# # # #         print("Администратор")
# # # #     case "user":
# # # #         print("Пользователь")
# # # #     case _:
# # # #         print("Пароль не верен ")
# # #
# # # # day = 'понедельник'
# # # # time = 13
# # # #
# # # # match day:
# # # #     case 'понедельник' | ' вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
# # # #         print("Рабочий день")
# # # #     case 'суббота' | 'воскресенье':
# # # #         print("Выходной день")
# # # #     case _:
# # # #         print("Такого дня недели не существует или нерабочее время")
# # #
# # # #
# # # # a, b = 30, 20
# # # # print(a if a < b else b)
# # #
# # #
# # # # a, b = 10, 5
# # # # print("На ноль делить нельзя" if b == 0 else a / b)
# # #
# # # # a = int(input("Введите количество копеек от 1 до 99: "))
# # # # cop = a
# # # # if 11 <= cop <= 14:
# # # #     print(a, "копеек")
# # # # elif 1 <= a <= 10 or 15 <= a <= 99:
# # # #     cop = cop % 10
# # # #     if cop == 1:
# # # #         print(a, "копейка")
# # # #     elif 2 <= cop <= 4:
# # # #         print(a, "копейки")
# # # #     else:
# # # #         print(a, "копеек")
# # # # else:
# # # #     print("Введите количество копеек от 1 до 99")
# # #
# # # #
# # # # n = input("Введите первое число: ")
# # # # m = input("Введите второе число: ")
# # # #
# # # # try:
# # # #     n = int(n)
# # # #     m = int(m)
# # # # except ValueError:
# # # #     n = str(n)
# # # # #     m = str(m)
# # # # # finally:
# # # # #     print(n + m)
# # # #
# # # # n = int(input("Укажите количество символов: "))
# # # # i = 0
# # # # while i < n:
# # # #     print("*", end=" ")
# # # #     i += 1
# # # #
# # # # lst = [10, 2, 2, 2, 2, 3, 3, 8, 8, 9, 9, 9, 10]
# # # # st = {i for i in lst if i % 2 == 0}
# # # # print(st)
# # # # lst2 = list(st)
# # # # print(lst2)
# # #
# # #
# # # # lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # #
# # # # lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # # # print({i for i in lst if 'a' in i})
# # # # print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# # # # print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
# # # # lst2 = []
# # # # for i in lst:    if
# # # # i[1] == "c":
# # # # if i[0] == "a":
# # # #     lst2.append("A" + i[1:])        else:
# # # #     lst2.append("B" + i[1:])
# # # # print(lst2)
# # #
# # # # lst2 = []
# # # # for i in lst:    if
# # # # i[1] == "c":
# # # # if i[0] == "a":
# # # #     lst2.append("A" + i[1:])        else:
# # # #     lst2.append("B" + i[1:])
# # # # print(lst2)
# # #
# # # #
# # # # s1 = {1, 2}
# # # # s2 = {3}
# # # # s3 = {4, 5}
# # # # s4 = {3, 2, 6}
# # # # s5 = {6}
# # # # s6 = {7, 8}
# # # # s7 = {9, 8}
# # #
# # # #
# # # # s1 = {1, 2}
# # # # s2 = {3}
# # # # s3 = {4, 5}
# # # # s4 = {3, 2, 6}
# # # # s5 = {6}
# # # # s6 = {7, 8}
# # # # s7 = {9, 8}
# # # #
# # # # s1 = "Hello"
# # # # s2 = "How are you"  # a = set(s1) & set(s2)# print(a)s1 = set(s1)print(s1)s2 = set(s2)print(s2)a = s1 & s2for i in a:
# # # # print(i, end=" ")
# # # #
# # # # s1 = "Hello"
# # # # s2 = "How are you"  # a = set(s1) & set(s2)# print(a)s1 = set(s1)print(s1)s2 = set(s2)print(s2)a = s1 & s2for i in a:
# # # # # print(i, end=" ")
# # #
# # # #
# # # # lst = ["one", "two"]
# # # # d = {"first": "one", "second": "two"}
# # # # print(lst)
# # # # print(d)
# # #
# # # #
# # # # try:
# # # #     del d[key]except KeyError:
# # # #     print("Элемента с ключом", key, "нет в словаре")
# # # # print(d)
# # #
# # #
# # # # d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# # #
# # # #
# # # # goods = {'1': ['Core-i3-4330', 9, 4500], '2': ['Core i5-4670K', 3, 8500], '3': ['AMD FX-6300', 6, 3700],
# # # #          '4': ['Pentium G3220', 8, 2100], '5': ['Core i5-3450', 5, 6400], }
# # #
# # # #
# # # # goods = {'1': ['Core-i3-4330', 9, 4500], '2': ['Core i5-4670K', 3, 8500], '3': ['AMD FX-6300', 6, 3700],
# # # #          '4': ['Pentium G3220', 8, 2100], '5': ['Core i5-3450', 5, 6400], }
# # # #
# # # # for i in goods:    print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
# # #
# # # # d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# # # #
# # # #
# # # # d = {"first": {1: "one", 2: "two", 3: "three"}, "second": {4: "four", 5: "five"}}
# # # # print(d)
# # # #
# # # #
# # # # for x, y in d.items():    print(x)
# # # # for i, j in y.items():        print("\t", i, ": ", j, sep="")
# # #
# # # #
# # # # a = int(input("Введите число копеек: "))
# # # # cop = a
# # # # if 11 <= cop <= 14:
# # # #     print(a, "копеек")
# # # # elif cop = cop % 10:
# # # #     cop <= 1:
# # # #     print(a, "копейка"
# # # #
# # # # res = 1
# # # # while True:
# # # #     n = int(input("Введите  числа: "))
# # # #     if n == 0:
# # # #         break
# # # #     res = n * res
# # # # print(res)
# # # # print("Цикл завершен")
# # # #
# # #
# # # #
# # # # n = int(input("Введите количество символов: "))
# # # # symbol = input("Тип символа: ")
# # # # orient = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
# # # #
# # # # i = 0
# # # #
# # # # while i < n:
# # # #     if orient == 1:
# # # #         print(symbol)
# # # #     else:
# # # #         print(symbol, end=" ")
# # # #     i += 1
# # # #       #Списки
# # # # bicycless = ['trek', 'cannondale', 'redline', 'specialized']
# # # # # print(bicycless[1].title())
# # # # # print(bicycless[3].title())
# # # # # print(bicycless[-1].title())
# # # # # print(bicycless[-2].title())
# # # # # print(bicycless[-3].title())
# # # # # print(bicycless[-4].title()
# # # # message = f"My first bicycles was a {bicycless[3].title()}"
# # # # print(message)
# # #
# # # # names = ['nina', 'aleksandra', 'svetlana', 'sasha', 'ferenc']
# # # # # print(names[0].title())
# # # # # print(names[1].title())
# # # # # print(names[2].title())
# # # # # print(names[3].title())
# # # # # print(names[4].title())
# # # # messages1 = f"i love my mam {names[0].title()}"
# # # # messages = f"my names is {names[1].title()} "
# # # # messages2 = f"I love my sister {names[2]} "
# # # # messages3 = f"Hello my perfect friend {names[3].title()}"
# # # # messages4 = f"Hi my love husband {names[4].title()}"
# # # # print(messages1)
# # # # print(messages)
# # # # print(messages2)
# # # # print(messages3)
# # # # print(messages4)
# # #
# # # # moto = ['honda', 'ural', 'suzuki', 'trek']
# # # # messages = f"Я хотел бы купить мотоцикл {moto[0].title()}"
# # # # messages1 = f"Мой первый мотоцикл {moto[1].title()}"
# # # # messages2 = f"Моим последним мотоциклом был {moto[3].title()}"
# # # # messages3 = f"Отличный мотоцикл {moto[2].title()}"
# # # # print(messages)
# # # # print(messages1)
# # # # print(messages2)
# # # # # print(messages3)
# # # # moto = ['honda', 'ural', 'suzuki', 'trek']
# # # # print(moto)
# # # # # moto[2] = 'ducati'
# # # # # print(moto)
# # # # # metod append
# # # # moto.append('ducati')
# # # # print(moto)
# # # # moto = []
# # # # moto.append('honda')
# # # # moto.append('ural')
# # # # moto.append('suzuki')
# # # # print(moto)
# # # # moto = ['honda', 'ural', 'suzuki', 'trek']
# # # # moto.insert(2, 'ducati')
# # # # moto.insert(3, 'ural')
# # # # moto.insert(6, 'alex')
# # # # print(moto)
# # #
# # # # Удаление
# # # # del moto[0]
# # # # del  moto[2]
# # # # del moto[1]
# # # # print(moto)
# # #
# # # # moto = ['honda', 'ural', 'suzuki', 'trek', 'ducati']
# # # # print(moto)
# # # # # motobig = moto.pop(1)
# # # # # print(f"My first motocycles was a {motobig.title()}")
# # # #
# # # # expensive = 'suzuki'
# # # # moto.remove(expensive)
# # # # print(moto)
# # # # print(f"\nA {expensive.title()} is too expensive for me. ")
# # #
# # #
# # # # guest = ['nina', 'sasha', 'sveta', 'ferenc']
# # # # print(guest)
# # # # # top = f" Дорогая {guest[0].title()} хочу пригласить тебя на обед. "
# # # # print(top)
# # # # top1 = f"Дорогая {guest[1].title()} приглашаю тебя на обед. "
# # # # print(top1)
# # # # top2 = f"Дорогая {guest[2].title()} люблю тебя и приглашаю на обед. "
# # # # print(top2)
# # # # top3 = f"Дорогой муж {guest[3].title()} приглашаю тебя на наш обед. "
# # # # print(top3)
# # # # print(f"{guest[3].title()} не сможет быть, потому что работает. ")
# # # # guest[3] = 'sasha'
# # # # print(guest)
# # # # top = f" Дорогая {guest[0].title()} хочу пригласить тебя на обед. "
# # # # print(top)
# # # # top1 = f"Дорогая {guest[1].title()} приглашаю тебя на обед. "
# # # # print(top1)
# # # # top2 = f"Дорогая {guest[2].title()} люблю тебя и приглашаю на обед. "
# # # # print(top2)
# # # # top3 = f"Дорогой  {guest[3].title()} приглашаю тебя на наш обед. "
# # # # print(top3)
# # #
# # # #
# # # # guest = ['nina', 'sasha', 'sveta', 'ferenc']
# # # # print(guest)
# # # # print(f"Мы хотим пригласить еще троих гостей.")
# # # # guest.insert(0,'sasha')
# # # # print(guest)
# # # # guest.insert(2, 'varvara')
# # # # print(guest)
# # # # guest.append('nastya')
# # # # print(guest)
# # # # new = f"Дорогой {guest[0].title()}, хотим пригласить тебя на обед."
# # # # print(new)
# # # # new1 = f"Дорогая {guest[1].title()}, хотим пригласить тебя на обед."
# # # # print(new1)
# # # # new2 = f"Дорогая {guest[2].title()}, хотим пригласить тебя на обед."
# # # # print(new2)
# # # # new3 = f"Дорогая {guest[3].title()}, хотим пригласить тебя на обед."
# # # # print(new3)
# # # # new4 = f"Дорогая {guest[4].title()}, хотим пригласить тебя на обед."
# # # # print(new4)
# # # # new5 = f"Дорогой {guest[5].title()}, хотим пригласить тебя на обед."
# # # # print(new5)
# # # # new6 = f"Дорогая {guest[6].title()}, хотим пригласить тебя на обед."
# # # # print(new6)
# # # # print(f"Извините, но на обед приглашаются всего два гостя.")
# # # # star = guest.pop()
# # # # print(f"Уважаемая {star.title()} нам очень жаль.")
# # # # star = guest.pop()
# # # # print(f"Уважаемый {star.title()} приносим извинения")
# # # # star = guest.pop()
# # # # print(f"Уважаемая {star.title()} приносим извинения")
# # # # star = guest.pop()
# # # # print(f"Уважаемый {star.title()} приносим извинения")
# # # # star = guest.pop()
# # # # print(f"Уважаемый {star.title()} приносим извинения")
# # # #
# # # # guest = ['nina', 'sasha']
# # # # print(guest)
# # # # print(f"Увжаемая {guest[0].title()} ранее приглашение остается в силе.")
# # # # print(f"Увжаемая {guest[1].title()} ранее приглашение остается в силе.")
# # # # del guest[0]
# # # # print(guest)
# # # # del guest[0]
# # # # print(guest)
# # #
# # # # print("Here is original list: ")
# # # # print(guest)
# # # #
# # # # print("\nHere is the sorted list: ")
# # # # print(sorted(guest))
# # # #
# # # # print("\nHere is the original list again: ")
# # # # print(guest)
# # # #
# # # # guest = ['nina', 'sasha', 'sveta', 'ferenc']
# # # #
# # # # guest.reverse()
# # # # print(guest)
# # # #
# # # # world = ['russia', 'argentina', 'chili', 'hungary', 'poland']
# # # # # print("Here is original list: ")
# # # # print(world)
# # # # #
# # # # # print("\nHere is the sorted list: ")
# # # # # print(sorted(world))
# # # # #
# # # # # print("\nHere is original list:")
# # # # # print(world)
# # # # #
# # # # # print("\nHere is revers list: ")
# # # # world.reverse()
# # # # print(world)
# # # # world.reverse()
# # # # print(world)
# # #
# # # # world = ['russia', 'argentina', 'chili', 'hungary', 'poland']
# # # # print(world)
# # # # world.sort()
# # # # print(world)
# # # # world.sort(reverse=True)
# # # # print(world)
# # # #
# # # # guest = ['nina', 'sasha', 'sveta', 'ferenc']
# # # # print(guest)
# # # # leight = len(guest)
# # # # print(leight)
# # #
# # # # lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # # # print([i for i in lst if 'a' in i])
# # #
# # # #
# # # # magicians = ['alice', 'david', ' carolina']
# # # # for magician in magicians:
# # # #     print(f"{magician.title()} , that is great trick!")
# # # #     print(f"I cannot see your next trick, {magician.title()}.\n")
# # # #
# # # #     print("Thank you, everyone. That was a great magic show!")
# # # #
# # # # # message = "Hello Puthon World: "
# # #
# # # # print(message)
# # # #
# # #
# # # # PIZZA
# # # #
# # # # pizza = ['salami', 'chess', 'meet', 'gombo']
# # # # for flower in pizza:
# # # #     # print(flower)
# # # #     print(f"I like {flower} pizza")
# # # #
# # # # print(f"\nI really love {flower} pizza!")
# # # # print(f"\nI really love {flower} pizza!")
# # # # print(f"\nI really love {flower} pizza!")
# # # # print(f"\nI really love {flower} pizza!")
# # #
# # #
# # # # animals = ['lion', 'dog', 'wulf', 'cat']
# # # # for animal in animals:
# # # #
# # # #     print(f"A {animal} would make a great pet\n")
# # # # print("Any of these animals would make a great pet!")
# # #
# # # #
# # # # for value in range(6):
# # # #     print(value)
# # #
# # # # numbers = list(range(2, 11, 2))
# # # # print(numbers)
# # # #
# # # # squares = []
# # # # for value in range(1, 11):
# # # #
# # # #     squares.append(value ** 2)
# # # # print(squares)
# # # # squares = [value ** 2 for value in range(1, 11)]
# # # # print(squares)
# # # #
# # # # n = int(input("Введите число: "))
# # # # for value in range(1, 1000001):
# # # #     print(value)
# # # #
# # # # res = 1
# # # # while True:
# # # #     n = int(input("Введите числа: "))
# # # #
# # # #     if n == 0:
# # # #         break
# # # #     res *= n
# # # # print("Результат: ", res)
# # # #
# # # # i = 1
# # # # while i < 5:
# # # #     print("Внешний цикл: i=", i)
# # # #     j = 1
# # # #     while j < 4:
# # # #         print("\tВнутренний цикл: j=", j)
# # # #         j += 1
# # # #     i += 1
# # #
# # # #
# # # # i = 1
# # # # while i < 10:
# # # #     j = 1
# # # #     while j < 10:
# # # #         print(i, "*", j, "=", i * j, end="\t\t")
# # # #         j += 1
# # # #     print()
# # # #     i += 1
# # #
# # # #
# # # # n = int(input("Введите количество символов: "))
# # # # symbol = input("Тип символа: ")
# # # # orient = input("\n0 - горизонтальная,\n1 - вертикальная, \n Ориентация линии: ")
# # # #
# # # # i = 0
# # # # while i < n:
# # # #     if orient == 1:
# # # #         print(symbol)
# # # #     else:
# # # #         print(symbol, end=" ")
# # # #     i += 1
# # #
# # # #
# # # # lst = [10, 20, 30]
# # # # tpl = (10, 20, 30)
# # # # print(lst.__sizeof__())
# # # # print(tpl.__sizeof__())
# # # #
# # # # def slicer(tpl, el):
# # # #
# # # #
# # # # #
# # # # # print(slicer((1, 2, 3), 8))
# # # # # print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# # # # # print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# # # #
# # # # #
# # # # # dict_sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694}, "Tom": {"N": 4832, "S": 6786, "E": 4773, "W": 3612},
# # # # #               "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
# # # # #               "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
# # # # #
# # # # # g = {'John': {"N": 3056, "S": 8463, "E": 8441, "W": 2694}, 'Tom': {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
# # # # #      'Anne': {"N": 5239, "S": 4802, "E": 5820, "W": 1859}, 'Fionna': {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
# # # # # for x, y in g.items():    print(x)
# # # # # for i, j in y.items():        print("\t", i, ": ", j, sep="")
# # # # #
# # # # # lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# # # # #
# # # # # one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# # # # # two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
# # # # #
# # # # # lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # # # #
# # # # # letter = ['b', 'a', 'd', 'c']
# # # # # number = [3, 4, 1, 2]
# # # # #
# # # # # one = {"один": 1, "два": 2}
# # # # # two = {"три": 3, "четыре": 4}
# # # # #
# # # # #
# # # # # def info(**data):    for
# # # # #
# # # # #
# # # # # k, v in data.items(): print(k, ":", v)
# # # # # print()
# # # # # info(name="Irina", surname="Vetrova", age=22)
# # # # # info(name="Igor", phone="456789", age=22, email="igor@mail.ru")
# # # #
# # # # #
# # # # # countries = (
# # # # #     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))), ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),)
# # # # # print(countries)
# # # # # for country in countries:
# # # # #     country_name, country_population, cities = country
# # # # #     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
# # # # # for city in cities:        city_name, city_population = city
# # # # # print("\tГород: ", city_name, ", население = ", city_population, sep="")
# # # # #
# # # # # countries = (
# # # # #     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))), ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),)
# # # # #
# # # # #
# # # # #
# # # # # print(countries)
# # # # # for country in countries:
# # # # #     country_name, country_population, cities = country
# # # # #     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
# # # # #     for city in cities:
# # # # #         city_name, city_population = city
# # # # #         print("\tГород: ", city_name, ", население = ", city_population, sep="")
# # # #
# # # # #
# # # # # def outer(a1, b1, a2, b2):    a = 0
# # # # #
# # # # #
# # # # # b = 0
# # # # #
# # # # #
# # # # # def inner():        a = a1 + a2
# # # # #
# # # # #
# # # # # b = b1 + b2
# # # # #
# # # # # from random import randint
# # # # #
# # # # # def ran (a, b):
# # # # #     return tuple(randint(a, b) for i in range(10))
# # # # #
# # # # # tpl1 = ran(0, 5)
# # # # # print(tpl1)
# # # # #
# # # # # tpl2 = ran(-5, 0)
# # # # # print(tpl2)
# # # # #
# # # # # tpl3 = tpl1 + tpl2
# # # # # print(tpl3)
# # # # # print("0=", tpl3.count(0))
# # # #
# # # #
# # # # # Анонимные функции (Lambda-выражения)# def func(x, y):#
# # # # # return x + y### print(func(1, 2))##
# # # # # print((lambda x, y: x + y)(1, 2))## func = lambda x, y: x + y##
# # # # # print(func(1, 2))### func = (lambda x, y: x + y)(1, 2)#
# # # # # print(func)print((lambda a, b, c: a + b + c)(10, 20, 30))
# # # # # print((lambda a, b, c=3: a + b + c)(10, 20))
# # # # # print((lambda a, b=2, c=3: a + b + c)(10))
# # # # # print((lambda a=1, b=2, c=3: a + b + c)())
# # # # #
# # # # # print((lambda a, b, c: a + b + c)(10, 20, 30))
# # # # # print((lambda a, b, c=3: a + b + c)(10, 20))
# # # # # print((lambda a, b=2, c=3: a + b + c)(10))
# # # # # print((lambda a=1, b=2, c=3: a + b + c)())
# # # #
# # # # #
# # # # # players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
# # # # #            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
# # # # #            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
# # # # #            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
# # # #
# # # #
# # # # # lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# # # #
# # # # d = {1: lambda: print("Понедельник"),
# # # #      2: lambda: print("Вторник"),
# # # #      3: lambda: print("Среда"),
# # # #      4: lambda: print("Четверг"),
# # # #      5: lambda: print("Пятница"),
# # # #      6: lambda: print("Суббота"),
# # # #      7: lambda: print("Воскресенье")}
# # # #
# # # # # from random import randint# s = (lambda lst: [randint(10, 20) for i in range(10)])([])# print(s)#
# # # # # print([randint(10, 20) for i in range(10)])#
# # # # # print([i * 2 for i in [1, 2, 3, 4, 5, 6]])
# # # #
# # # #
# # # # # from random import randint# s = (lambda lst: [randint(10, 20) for i in range(10)])([])#
# # # # # print(s)#
# # # # # print([randint(10, 20) for i in range(10)])#
# # # # # print([i * 2 for i in [1, 2, 3, 4, 5, 6]])
# # # #
# # # #
# # # # st = ['a', 'b', 'c', 'd', 'e', 'w']
# # # # num = [1, 2, 3, 4, 5]
# # # # print(dict(map(lambda x, y: (x, y), st, num)))
# # # # print(list(map(lambda x, y: (x, y), st, num)))
# # # #
# # # # t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# # # #
# # # # lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# # # # print(list(filter(lambda s: s > 75, lst)))
# # # #
# # # # nums = [45, 55, 60, 37, 100, 105, 220]
# # # #
# # # # from random import randintlst = [randint(1, 40) for i in range(10)]
# # # # print(lst)
# # # # print(list(filter(lambda a: (a >= 10) and a <= 20, lst)))
# # # # print(list(filter(lambda a: 10 <= a <= 20, lst)))
# # # #
# # # #
# # # # def my_decorator(func):    def
# # # #
# # # #
# # # # func_wrapper(): print("Код до функции")
# # # # func()
# # # # print("Код после функции")
# # # # return func_wrapperdef
# # # # func_test(): print("Hello, I am func 'func_test'")
# # # # test = my_decorator(func_test)
# # # # test()
# # # #
# # # #
# # # # def bold(fn):    def
# # # #
# # # #
# # # # wrap():
# # # # return "<b>" + fn() + "</b>"
# # # # return wrapdef
# # # # hello():
# # # # return "text"
# # # # print(hello())
# # # #
# # # #
# # # # def args_dec(fn):    def
# # # #
# # # #
# # # # wrap(x, y): print("Сложение:", x, "и", y, "=", end=" ")
# # # # fn(x, y)
# # # # return wrapdef
# # # # summa(a, b): print(a + b)
# # # # summa(5, 2)
# # # #
# # # #
# # # # def multiply(arg):    def
# # # #
# # # #
# # # # my_decorator(func):
# # # #
# # # #
# # # # def wrap(*args, **kwargs):            return func(*args, **kwargs)
# # # #
# # # #
# # # # return wrap
# # # # return my_decorator @ multiply(3)
# # # #
# # # #
# # # # def return_num(num):    return numprint("Результат:", return_num(5))
# # # #
# # # #
# # # # print(
# # # #     bin(18))  # 0b10010 - двоичная система счисленияprint(oct(18))  # 0o22 - восьмеричная система счисленияprint(hex(18))  # 0x12 - шестнадцатеричная система счисленияprint(0b10010)
# # # # # print(0o22)print(0x12 + 0b10010 + 4)
# # # #
# # # # print(e)  # print(e * 3)#
# # # # # print("y" in e)#
# # # # # print("a" in e)#
# # # # # print(e[-1])#
# # # # # print(e[1:3])
# # # #
# # # # q = 'Pyt'
# # # # w = "hon"
# # # # e = q + w
# # # #
# # # # str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# # # #
# # # #
# # # #
# # # # s = "hello, WORLD! I am learning Python."
# # # #
# # # # st = "один два"print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")])
# # # #
# # # # str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# # # #
# # # # s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# # # #
# # # # st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# # # #
# # # #
# # # # st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # # #
# # # # reg = r"\w+\s*=[^;]+"
# # # #
# # # # reg = r"\w+\s*=[^;]+"
# # # #
# # # # st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# # # #
# # # # # text = """# one# two# """#
# # # # # print(re.findall(r"one.\w+", text))#
# # # # # print(re.findall(r"one.\w+", text, re.DOTALL))#
# # # # # print(re.findall(r"one$", text))# print(re.findall(r"one$", text, re.MULTILINE))
# # # # #
# # # # # names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# # # # print("Текст в локальном репозитории")
# # # # print("Мир во всём мире")
# # # # print("Пусть всегда будет солнце!")
# # #
# # # # print("Код написан на новом устройстве")
# # #
# # # # Файлы
# # # # f = open(r"C:\Users\User\Desktop\python\text.txt", "r")
# # # # f = open("text.txt")
# # # # print(*f)
# # # # print(f)
# # # # print(f.mode)
# # # # print(f.name)
# # # # print(f.encoding)
# # # #
# # # #
# # # # print(f.closed)
# # # # # f.close()
# # # # f = open("text.txt", "r")
# # # # print(f.read(3))
# # # # # print(f.read())
# # # # # f.close()
# # # # #
# # # # # Файл — именованная область данных на носителе информации, используемая как базовый
# # # # # объект взаимодействия с данными в операционных системах.
# # # #
# # # # # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока
# # # # # №9\nСтрока №10\n"
# # # # #
# # # # f = open("texstnew.txt")
# # # # # # f = open(r"C:\Users\User\Desktop\python\texstnew.txt", "r")
# # # # print(*f)
# # # # print(f)
# # # # # print(f.mode)
# # # # print(f.name)
# # # # print(f.encoding)
# # # #
# # # # f.close()
# # # # print(f.closed)
# # #
# # #
# # # # f = open("texstnew.txt", "r")
# # # # print(f.read())
# # # # f.close()
# # #
# # # # print(f.read())
# # # # print(f.readline())
# # # # print(f.readline(8))
# # # # print(f.readline())
# # # # print(f.readlines())
# # #
# # # # f = open("xyz.txt")
# # # # for line in f:
# # # #     print(line)
# # # # f.close()
# # #
# # # # f.write("This is line1.\nThis is line2.\nThis is line3.\n")
# # # # #
# # # # lines = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]
# # # # f = open("lines.txt", "w")
# # # # # f.writelines(lines)
# # # # f.close()
# # # #
# # # # lines = [str(i) for i in range(10, 1000, 15)]
# # # # print(lines)
# # # #
# # # # f = open("lines.txt", "w")
# # # # for index in lines:
# # # #     f.write(index)
# # import os
# # from fileinput import close
# #
# # # # file = "text2.txt"
# # f = open("texstnew.txt", "w", encoding="utf-8")
# # f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# # f.close()
# # #
# # # file = "text2.txt"
# # #
# # from dz.dz22.dz22 import read_line
# #
# # file = "text2.txt"
# # f = open(file, "w", encoding="utf-8")
# # f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# # f.close()
# #
# # f = open(file, "r", encoding="utf-8")
# # read_line = f.readlines()
# # print(read_line)
# # read_line[1] = "Hello world!"
# # print(read_line)
# # f.close()
# #
# # f = open(file, "w", encoding="utf-8")
# # f.write(read_line)
# # f.close()
# # # # #
# import os
#
# # # f = open(file, "r")
# # # read_line = f.readlines()
# # # print(read_line)
# # # read_line[1] = "Hello world!\n"
# # # print(read_line)
# # # f.close()
# # #
# # # f = open(file, "w")
# # # f.writelines(read_line)
# # # f.close()
# #
# #
# # # f = open("text.txt", "r")
# # # print(f.read(3))
# # # print(f.tell())  # возвращает текущую позицию условного курсора в файле
# # # print(f.seek(1))  # перемещает условный курсор в заданную позицию
# # # print(f.read())
# # # print(f.tell())
# # # f.close()
# #
# #
# # # f = open("text5.txt", "a")
# # # print(f.write("I am learning Python"))
# # # print(f.seek(0))
# # # print(f.write("--new string--"))
# # # # print(f.read())
# # # f.close()
# #
# # # with open("text.txt", "w") as f:
# # #     print(f.write("0123456789"))
# # # print(f.closed)
# #
# # # lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.04]
# # #
# # #
# # # def get_line(lt):
# # #     lt = list(map(str, lt))
# # #     return " ".join(lt)
# # #
# # #
# # # with open("res.txt", "w") as f:
# # #     f.write(get_line(lst))
# # #
# # # print("Конец программы")
# #
# #
# # # with open("res.txt") as f:
# # #     nums = f.read()
# # #
# # # print(nums)
# # #
# # # print(map(float, nums.split()))
# # # print(list(map(float, nums.split())))
# # # print(sum(list(map(float, nums.split()))))
# # # print(sum(map(float, nums.split())))
# #
# #
# # # with open("res2.txt", "w") as f:
# # #     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект "
# # #             "с данными в операционных системах.")  # взаимодействия
# # #
# # #
# # # def longest_words(file):
# # #     with open(file) as text:
# # #         w = text.read().split()
# # #         print(w)
# # #         max_length = len(max(w, key=len))
# # #         print(max_length)
# # #         res = [word for word in w if len(word) == max_length]
# # #         if len(res) == 1:
# # #             return res[0]
# # #         return res
# # #
# # #
# # # print(longest_words("res2.txt"))
# #
# # # f = open("text1.txt", "r")
# # # print(f.read(3))
# # # print(f.tell())
# # # f,close()
# # # #
# # # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# # # with open("one.txt", "w", encoding="utf-8") as f:
# # #     f.write(text)
# # #
# # # with open("one.txt", "r", encoding="utf-8" ) as fr, open("two.txt", "w",encoding="utf-8" ) as fw:
# # #     for line in fr:
# # #         line = line.replace("Строка", "Линия -")
# # #         fw.write(line)
# #
# #
# # # import os
# #
# # # print(os.getcwd())  # путь к текущей директории
# # #
# # # print(os.listdir())  # возвращает список директорий и файлов
# # # print(os.listdir(".."))
# # # print(os.listdir(".venv"))
# #
# # # os.mkdir("folder")  # создать папку
# # # os.rmdir("folder.txt")  # удалить папку
# #
# # # os.makedirs("nested1/nested2/nested3")  # создает директорию с промежуточными папками
# #
# # # os.remove("xyz.txt")  # удалить файл
# #
# # # os.rename("two.txt", "www.txt")  # переименовали файл
# #
# # # os.rename("www.txt", "folder/www.txt")  # переместили файл в заданную папку
# #
# # # os.renames("text4.txt", "test/text4.txt")  # переместили файл, создавая промежуточные папки
# #
# # # import  os
# # # for root, dirs, files in os.walk("nested1", topdown=False):
# # #     print("Root:", root)
# # #     print("\tdirs:", dirs)
# # #     print("\tFiles", files)
# # #
# # # import os.path
# # #
# # # print(os.path.split(r"C:\Users\User\Desktop\python\texstnew.txt"))
# # # print(os.path.split("C:\\Users\\User\\Desktop\\python\\texstnew.txt"))
# #
# # #
# # # import os
# # #
# # # dirs = [r"Work\F1", r"Work\F2\F21"]
# # # # for d in dirs:
# # # #     os.makedirs(d)
# # # files = {
# # #     "Work": ["w.txt"],
# # #     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
# # #     r"Work\F2\F21":  ["f211.txt", "f212.txt"]
# # # }
# # #
# # # for d, files in files.items():
# # #     for file in files:
# # #         file_path = os.path.join(d, file)
# # #         # print(file_path)
# # #         open(file_path, "w", encoding="utf-8").close()
# # #
# # # file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
# # #
# # # for file in file_with_text:
# # #     with open(file, "w", encoding="utf-8") as f:
# # #         f.write(f"Такой-то текст в {file}")
# # #
# # # def print_tree(root,topdown):
# # #     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
# # #     for root, directory, file_name in os.walk(root, topdown):
# # #         print(root)
# # #         print(directory)
# # #         print(file_name)
# # #     print("-" * 50)
# # #
# # # print_tree("Work", False)
# # # print_tree("Work", True)
# #
# # #
# # # import os
# # # import time
# # #
# # # file = "readme.md"
# # #
# # # # print(os.path.exists(r"C:\Users\User\Desktop\python\texstnew.txt"))
# # # # print(os.path.isfile(r"C:\Users\User\Desktop\python\texstnew.txt"))
# # # # print(os.path.isdir(r"C:\Users\User\Desktop\python\texstnew.txt"))
# # #
# # # print(os.path.getsize(file))# размер файла в байтах
# # # print(os.path.getatime(file))# возвращает время последнего доступа к файлу
# # # print(os.path.getmtime(file))#возвращает время последнего изменения файла
# # # print(os.path.getctime(file)) # возвращает время создания файла
# # #
# # # kb = os.path.getsize(file)
# # # a = os.path.getatime(file)
# # # m = os.path.getmtime(file)
# # # c = os.path.getctime(file)
# # #
# # # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# # # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# # # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# # # print(kb // 1024)
# #
# # # Обьектно-ориентированное програмирование
# # #
# # # # class Name:
# # # - свойства, поля (переменные)
# # # - методы (функции)
# # # атрибуты  = свойства + методы
# #
# # class Point:
# #     x = 1
# #     y = 2
# # #
# #
# # p1 = Point()
# # p1.x = 10
# # p1.y = 20
# #
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# #
# # p2 = Point()
# # print(p2.x, p2.y)
# # p2.x = 5
# # print(p2.__dict__)
# #
# # print(Point.__dict__)
#
# # class Point:
# #     x = 1
# #     y = 2
# #     def set_coord(self, x1, y1):
# #         self.x = x1
# #         self.y = y1
# # #
# #
# # p1 = Point()
# # print(type(p1))
# # p1.set_coord(5, 10)
# # Point.set_coord(p1, 20, 30)
# # print(p1.__dict__)
# #
# # p2 = Point()
# # p2.set_coord(100, 200)
# # print(p2.__dict__)
#
# #
# # class Human:
# #     name = "name"
# #     birthday = "00.00.0000"
# #     phone = "00-00-00"
# #     country = "country"
# #     city = "city"
# #     address = "street, house"
# #
# #     def print_info(self):
# #         print(" Персональные данные ".center(40, "*"))
# #         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
# #               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
# #               f"Город: {self.city}\nДомашний адрес: {self.address}")
# #         print("=" * 40)
# #     def input_info(self, first_name, birthday, phone, country,city, address):
# #         self.name = first_name
# #         self.birthday = birthday
# #         self.phone = phone
# #         self.country = country
# #         self.city = city
# #         self.address = address
# #
# #     def set_name(self, name): # устанавливаем новое имя
# #         self.name = name
# #
# #     def get_name(self): # получаем новое имя
# #         return self.name
# #
# #
# #
# # h1 = Human()
# # h1.print_info()
# # h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва",
# #               "Чистопрудный бульвар, 1A")
# # h1.print_info()
# # h1.set_name("Юлия")
# # h1.print_info()
# # print(h1.get_name())
# #
# #
# # class Person:
# #     skill = 10
# #
# #     def __init__(self, name, surname):
# #         self.name = name
# #         self.surname = surname
# #         # print("Инициализатор для", self.name, self.surname)
# #
# #     def __del__(self):
# #         print("Удаление экземпляра")
# #
# #     def print_info(self):
# #         print("Данные сотрудника:", self.name, self.surname)
# #
# #     def add_skill(self, k):
# #         self.skill += k
# #         print("Квалификация сотрудника:", self.skill, "\n")
# #
# #
# #
# # p1 = Person("Виктор", "Резник")
# # p1.print_info()
# # p1.add_skill(3)
# #
# # del p1
# # print()
# #
# # p2 = Person("Анна", "Долгих")
# # p2.print_info()
# # p2.add_skill(2)
# #
# # class Point:
# #     count = 0
# #
# #
# #     def __init__(self, x=0, y=0):
# #         self.x = x
# #         self.y = y
# # #         Point.count += 1
# # #
# # # p1 = Point()
# # p2 = Point()
# # p3 = Point()
# # print(Point.count)
# #
# # class Robot:
# #     k = 0
# #
# #     def __init__(self, name):
# #         self.name = name
# #         print("Инициализация робота:", self.name)
# #         Robot.k += 1
# #
# #     def __del__(self):
# #         print(self.name, "выключается!")
# #         Robot.k -= 1
# #
# #         if Robot.k == 0:
# #             print(self.name, "был последним")
# #         else:
# #             print("Работающих роботов осталось:", Robot.k)
# #
# #
# #     def say_hi(self):
# #         print("Приветствую! Меня зовут:", self.name)
# #
# #
# # droid1 = Robot("R2-D2")
# # droid1.say_hi()
# # print("Численность роботов:", Robot.k)
# #
# # droid2 = Robot("С-3PO")
# # droid2.say_hi()
# # print("Численность роботов:", Robot.k)
# #
# # droid3 = Robot("PC-30")
# # droid3.say_hi()
# # print("Численность роботов:", Robot.k)
# #
# # print("\nЗдесь роботы могут проделать какую-то работу\n")
# # print("Роботы закончили свою работу. Давайте их выключим.")
# #
# # del droid3
# # del droid2
# # del droid1
# #
# # print("Численность роботов:", Robot.k)
# #
# #
# # self.__x = self.__y = 0if Point.__check_value(x) and Point.__check_value(y):
# #
# # f = open("xyz1.txt", "w", encoding="utf-8")
# # f.write("This is line1.\nThis is line2.\nThis is line3.\n")
# # f.close()
#
# # f = open("xyz1.txt")
# # print(f.read())
#
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# #
# # print(f.readlines(15))
# # print(f.readlines())
# #
# # f = open("xyz1.txt")
# # for line in f:
# #     print(line)
# # f.close()
# #
# # lines1 = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]
# # f = open("lines1.txt", "w", encoding="utf-8")
# # f.writelines(lines1)
# # f.close()
# #
# # lines1 = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]
# #
# # lines1 = [str(i) for i in range(10, 1000, 15)]
# # print(lines1)
# #
# # f = open("lines1.txt", "w", encoding="utf-8")
# # for index in lines1:
# #     f.write(index + "\t")
# # f.close()
#
#
# # Замена строки
# #
# # file1 = "test.txt"
# # f = open("test.txt", "w", encoding="utf-8")
# # f.write("Замена строки в текстовом файле;\nзаменить строку в списке;\nзаписать список в файл;\n")
# #
# # f.close()
# #
# # f = open(file1, "r", encoding="utf-8")#
# # read_line = f.readlines()
# # print(read_line)
# # read_line[1] = "Hello world!\n"
# # print(read_line)
# # f.close()
# #
# # f = open(file1, "w", encoding="utf-8")
# # f.writelines(read_line)
# # f.close()
#
#
# #
#
# # Файлы
#
# # f = open("text.txt")
# # # f = open(r"E:\Python416\416\text.txt", "r")
# # print(*f)
# # print(f)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)
# # f.close()
# # print(f.closed)
#
#
# # f = open("text.txt", "r")
# # # print(f.read(3))
# # print(f.read())
# # f.close()
#
# # f = open("xyz.txt", "w")
# # f.write("This is line1.\nThis is line2.\nThis is line2.\n")
# # f.close()
#
# # f = open("xyz.txt")
# # print(f.read())
#
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
#
# # print(f.readlines(15))
# # print(f.readlines())
#
# # f.close()
#
#
# # f = open("xyz.txt")
# # for line in f:
# #     print(line)
# # f.close()
#
# # lines = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]
# #
# # f = open("lines.txt", "w")
# # f.writelines(lines)
# # f.close()
#
# # lines = [str(i) for i in range(10, 1000, 15)]
# # print(lines)
# #
# # f = open("lines.txt", "w")
# # for index in lines:
# #     f.write(index + "\t")
# # f.close()
#
# # file = "text2.txt"
# #
# # f = open(file, "w")
# # f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# # f.close()
# #
# #
# # f = open(file, "r")
# # read_line = f.readlines()
# # print(read_line)
# # read_line[1] = "Hello world!\n"
# # print(read_line)
# # f.close()
#
# # f = open(file, "w")
# # f.writelines(read_line)
# # f.close()
#
#
# # f = open("text.txt", "r")
# # print(f.read(3))
# # print(f.tell())  # возвращает текущую позицию условного курсора в файле
# # print(f.seek(1))  # перемещает условный курсор в заданную позицию
# # print(f.read())
# # print(f.tell())
# # f.close()
#
#
# # f = open("text5.txt", "a")
# # print(f.write("I am learning Python"))
# # print(f.seek(0))
# # print(f.write("--new string--"))
# # # print(f.read())
# # f.close()
#
# # with open("text.txt", "w") as f:
# #     print(f.write("0123456789"))
# # print(f.closed)
#
# # lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.04]
# #
# #
# # def get_line(lt):
# #     lt = list(map(str, lt))
# #     return " ".join(lt)
# #
# #
# # with open("res.txt", "w") as f:
# #     f.write(get_line(lst))
# #
# # print("Конец программы")
#
#
# # with open("res.txt") as f:
# #     nums = f.read()
# #
# # print(nums)
# #
# # print(map(float, nums.split()))
# # print(list(map(float, nums.split())))
# # print(sum(list(map(float, nums.split()))))
# # print(sum(map(float, nums.split())))
#
#
# # with open("res2.txt", "w") as f:
# #     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект "
# #             "с данными в операционных системах.")  # взаимодействия
# #
# #
# # def longest_words(file):
# #     with open(file) as text:
# #         w = text.read().split()
# #         print(w)
# #         max_length = len(max(w, key=len))
# #         print(max_length)
# #         res = [word for word in w if len(word) == max_length]
# #         if len(res) == 1:
# #             return res[0]
# #         return res
# #
# #
# # print(longest_words("res2.txt"))
#
#
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока
# # №8\nСтрока №9\nСтрока №10\n"
# # with open("one.txt", "w") as f:
# #     f.write(text)
# #
# # with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
# #     for line in fr:
# #         line = line.replace("Строка", "Линия -")
# #         fw.write(line)
#
#
# # import os
# #
# # # print(os.getcwd())  # путь к текущей директории
# # #
# # # print(os.listdir())  # возвращает список директорий и файлов
# # # print(os.listdir(".."))
# # # print(os.listdir(".venv"))
# #
# # # os.mkdir("folder")  # создать папку
# # # os.rmdir("folder.txt")  # удалить папку
# #
# # # os.makedirs("nested1/nested2/nested3")  # создает директорию с промежуточными папками
# #
# # # os.remove("xyz.txt")  # удалить файл
# #
# # # os.rename("two.txt", "www.txt")  # переименовали файл
# #
# # # os.rename("www.txt", "folder/www.txt")  # переместили файл в заданную папку
# #
# # os.renames("text4.txt", "test/text4.txt")  # переместили файл, создавая промежуточные папки
#
#
# # f = open("test3.txt", "w")
# # f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# # f.close()
# #
# # f = open("test3.txt", "r")
# # read_line = f.readlines()
# # print(read_line)
# # f.close()
# #
# # pos1 = int(input("pos1 = "))
# # pos2 = int(input("pos2 = "))
# #
# # if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
# #     read_line[pos1], read_line[pos2] = read_line[pos2],  read_line[pos1]
# # else:
# #     print("Такой строки нет")
# #
# # print(read_line)
# #
# # f = open("test3.txt", "w")
# # f.writelines(read_line)
# # f.close()
#
# # import os
# #
# # # print(os.walk("nested1"))
# # # for root, dirs, files in os.walk("nested1", topdown=False):
# # #     print("Root:", root)
# # #     print("\tdirs:", dirs)
# # #     print("\tFiles:", files)
# #
# # # import os.path
# #
# # print(os.path.split(r"E:\Python416\nested1\nested2\nested3\text5.txt"))
# #
# # print(os.path.join("nested1", r"E:\Python416", "nested2", "nested3", "text5.txt"))
#
#
# # import os
# #
# # dirs = [r"Work\F1", r"Work\F2\F21"]
# # # for d in dirs:
# # #     os.makedirs(d)
# #
# # files = {
# #     "Work": ["w.txt"],
# #     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
# #     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# # }
# #
# # for d, files in files.items():
# #     for file in files:
# #         file_path = os.path.join(d, file)
# #         # print(file_path)
# #         open(file_path, "w").close()
# #
# #
# # file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
# #
# # for file in file_with_text:
# #     with open(file, "w") as f:
# #         f.write(f"Такой-то текст в файле {file}")
# #
# #
# # def print_tree(root, topdown):
# #     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
# #     for root1, directory, file_name in os.walk(root, topdown):
# #         print(root1)
# #         print(directory)
# #         print(file_name)
# #     print("-" * 50)
# #
# #
# # print_tree("Work", False)
# # print_tree("Work", True)
#
# # import os
# # import time
# #
# # # print(os.path.exists(r"nested1\nested2\nested3\text5.txt"))
# # # print(os.path.isfile(r"nested1\nested2\nested3\text5.txt"))
# # # print(os.path.isdir(r"nested1\nested2\nested3"))
# #
# # file = "main.py"
# #
# # print(os.path.getsize(file))  # размер файла в байтах
# # print(os.path.getatime(file))  # возвращает время последнего доступа к файлу
# # print(os.path.getmtime(file))  # возвращает время последнего изменения файла
# # print(os.path.getctime(file))  # возвращает время создания файла
# #
# # kb = os.path.getsize(file)
# # a = os.path.getatime(file)
# # m = os.path.getmtime(file)
# # c = os.path.getctime(file)
# #
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# # print(kb // 1024)
#
# # class Point:
# #     x = 1  # 100
# #     y = 2
# #
# # #
# # # p1 = Point()
# # # p1.x = 10
# # # p1.y = 20
# # # # Point.x = 100
# # # print(p1.x, p1.y)
# # # print(p1.__dict__)
# # #
# # # p2 = Point()
# # # print(p2.x, p2.y)
# # # p2.x = 5
# # # print(p2.__dict__)
# # #
# # # print(Point.__dict__)
# #
# # def func():
# #     print("текст")
# #
# #
# # func()
# #
# #
# # class Point:
# #     """Класс для предоставления координат точек на плоскости"""
# #     x = 1
# #     y = 2
# #
# #     def set_coord(self, x1, y1):
# #         self.x = x1
# #         self.y = y1
#
#
# # p1 = Point()  # экземпляр класса (объект)
# # p1.set_coord(5, 3)
# # print(p1.__dict__)
# # # print(Point.__doc__)
# # # print(Point.__dict__)
# # print(type(p1))
# # print(type(5))
# # p1.x = 5
# # p1.y = 10
# # p1.set_coord(5, 10)
# # print(p1.__dict__)
# # print(p1.x)
# # # Point.set_coord(p1, 20, 30)
# # # print(p1.__dict__)
# # #
# # p2 = Point()
# # p2.set_coord(100, 200)
# # print(p2.__dict__)
# # print(p2.x)
# #
# # class Rectangle:
# #     def __init__(self, length, width):
# #         self.__length = length
# #         self__width = width
# #
# #     def __check_value(c):
# #         if isinstance(c, int) or isinstance(c, float):
# #             return True
# #         return False
# #
# #     def set__width(self, width):
# #         if Rectangle.__check_value(width):
# #             self.__width = width
# #
# #     def set_leught(self, length):
# #         if Rectangle.__check_value(length):
# #             self.__length = length
# #
# #     def get_wight(self):
# #         def width = width
# #
# #
# # f = open("xyz2.txt", "w", encoding="utf-8")
# # f.write("This is line1.\nThis is line2.\nThis is line3.\n")
# # f.close()
#
# # f = open("xyz2.txt")
# # print(f.read())
# # print(f.readline())
# # print(f.readline(8))
# # # print(f.readline())
# # print(f.readlines(15))# считывает элементы как список строк
# # print(f.readlines())
# #
# # f = open("xyz2.txt")
# #
# # f.close()
# #
# # import os
# #
# # # print(os.walk("Work"))
# # for root, dirs, files in os.walk("Work", topdown=False):
# #     print("Root:", root)
# #     print("\tdirs:", dirs)
# #     print("\tfiles:", files)
# #
# #
# # import os
# #
# #
# # dirs = [r"Work2\F1", r"Work2\F2\F21"]
# # # for d in dirs:
# # #     os.makedirs(d)
# #
# # files = {
# #     "Work2": ["w.txt"],
# #     r"Work2\F1": ["f11.txt", "f12.txt", "f13.txt"],
# #     r"Work2\F2\F21": ["f211.txt", "f212.txt"]
# # }
# # for d, files in files.items():
# #     for file in files:
# #         file_path = os.path.join(d, file)
# #         # print(file_path)
# #
# # open(file_path, "w", encoding="utf-8").close()
# # file_with_text = [r"Work2\w.txt", r"Work2\F1\f12.txt", r"Work2\F2\F21\f212.txt", r"Work2\F2\F21\f213.txt"]
# #
# # for file in file_with_text:
# #     with open(file, "w", encoding="utf-8") as f:
# #         f.write(f"Всем мира и любви! {file}")
# #
# #
# # def print_tree(root, topdown):
# #     print(f"Обход {root}{'сверху вниз' if topdown else 'снизу вверх'}")
# #     for root, directory, file_name in os.walk(root, topdown):
# #         print(root)
# #         print(directory)
# #         print(file_name)
# #     print("-" * 50)
# #
# # print_tree("Work2", False)
# # print_tree("Work2", True)
# #
# # import os
# #
# # print(os.path.exists(r"C:\Users\User\Desktop\python\Work2\F1\f12.txt"))
#
#
# #
# # class Human:
# #     name = "name"
# #     birthday = "00.00.0000"
# #     phone = "00.00.00"
# #     counrty = "country"
# #     city = "city"
# #     address = "street, house"
# #
# #     def print_info(self):
# #         print(" Персональные данные ".center(40, "*"))
# #
# #         print("=" * 40)
#
# #
# # h1 = Human()
# # h1.print_info()
# #
# # from abc import ABC, abstractmethod
# #
# #
# # class Currency(ABC):
# #     suffix = "RUB"
# #
# #     def __init__(self, value):
# #         self.value = value
# #
# #     @abstractmethod
# #     def convert_to_rub(self):
# #         pass
# #
# #     @abstractmethod
# #     def print_value(self):
# #         print(self.value, end=" ")
# #
# #     def print_info(self):
# #         self.print_value()
# #         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
# #
# #
# # class Dollar(Currency):
# #     rate_to_rub = 74.16
# #     suffix = "USD"
# #
# #     def convert_to_rub(self):
# #         return self.value * Dollar.rate_to_rub
# #
# #     def print_value(self):
# #         super().print_value()
# #         print(Dollar.suffix, end=" ")
# #
# #
# # class Euro(Currency):
# #     rate_to_rub = 90.14
# #     suffix = "EUR"
# #
# #     def convert_to_rub(self):
# #         return self.value * Euro.rate_to_rub
# #
# #     def print_value(self):
# #         super().print_value()
# #         print(Euro.suffix, end=" ")
# #
# #
# # d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# # e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# #
# # print("*" * 50)
# # for elem in d:
# #     elem.print_info()
# #
# # print("*" * 50)
# # for elem in e:
# #     elem.print_info()
# #
# import os
# # import time
# #
# # file_path = "nested1\\nested2\\test3.txt"
# #
# # if os.path.exists(file_path):
# #     directory, name = os.path.split(file_path)
# #     atime = os.path.getatime(file_path)
# #     t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))
# #     print(f"{name} ({directory}) - время последнего доступа к файлу {t}")
# # else:
# #     print(f"Файл {file_path} не существует")
#
# # import math
# #
# #
# # class Rectangle:
# #     def __init__(self, length, width):
# #         self.__length = length
# #         self.__width = width
# #
# #     def __check_value(c):
# #         if isinstance(c, int) or isinstance(c, float):
# #             return True
# #         return False
# #
# #     def set_width(self, width):
# #         if Rectangle.__check_value(width):
# #             self.__width = width
# #
# #     def set_length(self, length):
# #         if Rectangle.__check_value(length):
# #             self.__length = length
# #
# #     def get_width(self):
# #         return self.__width
# #
# #     def get_length(self):
# #         return self.__length
# #
# #     def get_area(self):
# #         return self.__length * self.__width
# #
# #     def get_perimeter(self):
# #         return 2 * (self.__length + self.__width)
# #
# #     def get_hypotenuse(self):
# #         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
# #
# #     def get_draw(self):
# #         # for i in range(self.__length):
# #         #     for j in range(self.__width):
# #         #         print("*", end="")
# #         #     print()
# #
# #         # for i in range(self.__length):
# #         #     print("*" * self.__width)
# #
# #         print(("*" * self.__width + "\n") * self.__length)
# #
# #
# # r1 = Rectangle(4, 12)
# # r1.set_width(9)
# # r1.set_length(3)
# # print("Длина прямоугольника:", r1.get_length())
# # print("Ширина прямоугольника:", r1.get_width())
# # print("Площадь прямоугольника:", r1.get_area())
# # print("Периметр прямоугольника:", r1.get_perimeter())
# # print("Гипотенуза прямоугольника:", r1.get_hypotenuse())
# # r1.get_draw()
#
# #
# # class Point:
# #     __slots__ = ["x", "y", "z"]
# #
# #     def __init__(self, x1, y1):
# #         self.x = x1
# #         self.y = y1
# #
# #
# # p1 = Point(5, 10)
# # p1.z = 1
# # print(p1.x, p1.y, p1.z)
# # # print(p1.__dict__)
#
#
# # class Point:
# #     def __init__(self, x, y):
# #         self.__x = x
# #         self.__y = y
# #
# #     def __check_value(c):
# #         if isinstance(c, int) or isinstance(c, float):
# #             return True
# #         return False
# #
# #     def __set_coord_x(self, x):
# #         # print("Вызов __set_coord_x")
# #         if Point.__check_value(x):
# #             self.__x = x
# #         else:
# #             print("Неверный формат данных")
# #
# #     def __get_coord_x(self):
# #         # print("Вызов __get_coord_x")
# #         return self.__x
# #
# #     def __del_coord_x(self):
# #         print("Удаление свойства")
# #         del self.__x
# #
# #     x = property(__get_coord_x, __set_coord_x, __del_coord_x)
# #
# #
# # p1 = Point(5, 10)
# # # print(p1.__set_coord_x(50))
# # # print(p1.__get_coord_x())
# # p1.x = 50  # set
# # print(p1.x)  # get
# # del p1.x  # del
# # print(p1.__dict__)
#
#
# # class Point:
# #     def __init__(self, x, y):
# #         self.__x = x
# #         self.__y = y
# #
# #     @staticmethod
# #     def __check_value(c):
# #         if isinstance(c, int) or isinstance(c, float):
# #             return True
# #         return False
# #
# #     @property
# #     def x(self):
# #         return self.__x
# #
# #     @x.setter
# #     def x(self, x):
# #         if Point.__check_value(x):
# #             self.__x = x
# #         else:
# #             print("Неверный формат данных")
# #
# #     @x.deleter
# #     def x(self):
# #         del self.__x
# #
# #     # x = property(__get_coord_x, __set_coord_x, __del_coord_x)
# #
# #
# # p1 = Point(5, 10)
# # p1.x = 50  # set
# # print(p1.x)  # get
# # del p1.x  # del
# # print(p1.__dict__)
#
#
# # class Person:
# #     def __init__(self, name, old):
# #         self.__name = name
# #         self.__old = old
# #
# #     @property
# #     def name(self):
# #         return self.__name
# #
# #     @name.setter
# #     def name(self, n):
# #         self.__name = n
# #
# #     @name.deleter
# #     def name(self):
# #         del self.__name
# #
# #     @property
# #     def old(self):
# #         return self.__old
# #
# #     @old.setter
# #     def old(self, year):
# #         self.__old = year
# #
# #     @old.deleter
# #     def old(self):
# #         del self.__old
# #
# #
# # p1 = Person("Irina", 26)
# # print(p1.__dict__)
# # p1.name = "Igor"
# # p1.old = 31
# # print(p1.__dict__)
# # # del p1.name
# # del p1.old
# # print(p1.__dict__)
#
#
# # class Point:
# #     __count = 0
# #
# #     def __init__(self, x=0, y=0):
# #         self.x = x
# #         self.y = y
# #         Point.__count += 1
# #
# #     @staticmethod
# #     def get_count():
# #         return Point.__count
# #
# #     # get_count = staticmethod(get_count)
# #
# #
# # p1 = Point()
# # p2 = Point()
# # p3 = Point()
# # p4 = Point()
# #
# # print(Point.get_count())
# # print(p1.get_count())
#
#
# # def inc(x):
# #     return x + 1
# #
# #
# # def dec(x):
# #     return x - 1
# #
# #
# # print(inc(10), dec(10))
# #
# #
# # class Change:
# #     @staticmethod
# #     def inc(x):
# #         return x + 1
# #
# #     @staticmethod
# #     def dec(x):
# #         return x - 1
# #
# #
# # ch = Change()
# # print(ch.inc(10), Change.dec(10))
#
#
# # class Numbers:
# #     @staticmethod
# #     def max(a, b, c, d):
# #         mx = a  # mx = 3
# #         if b > mx:  # 5 > 3
# #             mx = b  # mx = 5
# #         if c > mx:  # 7 > 5
# #             mx = c  # mx = 7
# #         if d > mx:  # 9 > 7
# #             mx = d  # mx = 9
# #         return mx
# #
# #     @staticmethod
# #     def min(*args):
# #         mn = args[0]  # 3
# #         for i in args:
# #             if i < mn:  # 9 < 3
# #                 mn = i
# #         return mn
# #
# #     # @staticmethod
# #     # def average(*args):
# #     #     return sum(args) / len(args)
# #
# #     @staticmethod
# #     def average(a, b, c, d):
# #         return (a + b + c + d) / 4
# #
# #     @staticmethod
# #     def factorial(n):
# #         fact = 1
# #         for i in range(1, n + 1):
# #             fact *= i
# #         return fact
# #
# #
# # print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# # print("Минимальное число:", Numbers.min(3, 5, 7, 9))
# # print("Среднее арифметическое:", Numbers.average(3, 5, 7, 9))
# # print("Факториал числа:", Numbers.factorial(5))
#
# # f = open("test3.txt", "w")
# # f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# # f.close()
# #
# # f = open("test3.txt", "r")
# # read_line = f.readlines()
# # print(read_line)
# # f.close()
# #
# # pos1 = int(input("pos1 = "))
# # pos2 = int(input("pos2 = "))
# #
# # if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
# #     read_line[pos1], read_line[pos2] = read_line[pos2],  read_line[pos1]
# # else:
# #     print("Такой строки нет")
# #
# # print(read_line)
# #
# # f = open("test3.txt", "w")
# # f.writelines(read_line)
# # f.close()
#
# # import os
# #
# # # print(os.walk("nested1"))
# # # for root, dirs, files in os.walk("nested1", topdown=False):
# # #     print("Root:", root)
# # #     print("\tdirs:", dirs)
# # #     print("\tFiles:", files)
# #
# # # import os.path
# #
# # print(os.path.split(r"E:\Python416\nested1\nested2\nested3\text5.txt"))
# #
# # print(os.path.join("nested1", r"E:\Python416", "nested2", "nested3", "text5.txt"))
#
#
# # import os
# #
# # dirs = [r"Work\F1", r"Work\F2\F21"]
# # # for d in dirs:
# # #     os.makedirs(d)
# #
# # files = {
# #     "Work": ["w.txt"],
# #     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
# #     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# # }
# #
# # for d, files in files.items():
# #     for file in files:
# #         file_path = os.path.join(d, file)
# #         # print(file_path)
# #         open(file_path, "w").close()
# #
# #
# # file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
# #
# # for file in file_with_text:
# #     with open(file, "w") as f:
# #         f.write(f"Такой-то текст в файле {file}")
# #
# #
# # def print_tree(root, topdown):
# #     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
# #     for root1, directory, file_name in os.walk(root, topdown):
# #         print(root1)
# #         print(directory)
# #         print(file_name)
# #     print("-" * 50)
# #
# #
# # print_tree("Work", False)
# # print_tree("Work", True)
#
# # import os
# # import time
# #
# # # print(os.path.exists(r"nested1\nested2\nested3\text5.txt"))
# # # print(os.path.isfile(r"nested1\nested2\nested3\text5.txt"))
# # # print(os.path.isdir(r"nested1\nested2\nested3"))
# #
# # file = "main.py"
# #
# # print(os.path.getsize(file))  # размер файла в байтах
# # print(os.path.getatime(file))  # возвращает время последнего доступа к файлу
# # print(os.path.getmtime(file))  # возвращает время последнего изменения файла
# # print(os.path.getctime(file))  # возвращает время создания файла
# #
# # kb = os.path.getsize(file)
# # a = os.path.getatime(file)
# # m = os.path.getmtime(file)
# # c = os.path.getctime(file)
# #
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# # print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# # print(kb // 1024)
#
# # class Point:
# #     x = 1  # 100
# #     y = 2
# #
# #
# # p1 = Point()
# # p1.x = 10
# # p1.y = 20
# # # Point.x = 100
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# #
# # p2 = Point()
# # print(p2.x, p2.y)
# # p2.x = 5
# # print(p2.__dict__)
# #
# # print(Point.__dict__)
#
# # class Point:
# #     """Класс для предоставления координат точек на плоскости"""
# #     x = 1
# #     y = 2
# #
# #     def set_coord(self, x1, y1):
# #         self.x = x1
# #         self.y = y1
# #
# #
# # p1 = Point()  # экземпляр класса (объект)
# # p1.set_coord(5, 3)
# # print(p1.__dict__)
# # # print(Point.__doc__)
# # # print(Point.__dict__)
# # print(type(p1))
# # print(type(5))
# # # p1.x = 5
# # # p1.y = 10
# # # p1.set_coord(5, 10)
# # # print(p1.__dict__)
# # # print(p1.x)
# # # # Point.set_coord(p1, 20, 30)
# # # # print(p1.__dict__)
# # # #
# # p2 = Point()
# # p2.set_coord(100, 200)
# # # print(p2.__dict__)
# # print(p2.x)
# #
# # class Human:
# #     name = "name"
# #     birthday = "00.00.0000"
# #     phone = "00-00-00"
# #     country = "country"
# #     city = "city"
# #     address = "street, house"
# #
# #     def print_info(self):
# #         print(" Персональные данные ".center(40, "*"))
# #         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
# #               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
# #               f"Город: {self.city}\nДомашний адрес: {self.address}")
# #         print("=" * 40)
# #
# #     def input_info(self, first_name, birthday, phone, country, city, address):
# #         self.name = first_name
# #         self.birthday = birthday
# #         self.phone = phone
# #         self.country = country
# #         self.city = city
# #         self.address = address
# #
# #     def set_name(self, name):  # устанавливаем новое имя
# #         self.name = name
# #
# #     def get_name(self):  # получаем имя
# #         return self.name
# #
# #
# # h1 = Human()
# # h1.print_info()
# # h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# # h1.print_info()
# # h1.set_name("Юлия")
# # h1.print_info()
# # print(h1.get_name())
#
# # class Person:
# #     skill = 10
# #
# #     def __init__(self, name, surname):  # инициализатор
# #         self.name = name
# #         self.surname = surname
# #         # print("Инициализатор для", self.name, self.surname)
# #
# #     def __del__(self):
# #         print("Удаление экземпляра")
# #
# #     def print_info(self):
# #         print("Данные сотрудника:", self.name, self.surname)
# #
# #     def add_skill(self, k):
# #         self.skill += k
# #         print("Квалификация сотрудника:", self.skill, "\n")
# #
# #
# # p1 = Person("Виктор", "Резник")
# # p1.print_info()
# # p1.add_skill(3)
# #
# # del p1
# # print()
# #
# # p2 = Person("Анна", "Долгих")
# # p2.print_info()
# # p2.add_skill(2)
#
# # class Point:
# #     count = 0
# #
# #     def __init__(self, x=0, y=0):
# #         self.x = x
# #         self.y = y
# #         Point.count += 1
# #
# #
# # p1 = Point()
# # p2 = Point()
# # p3 = Point()
# # print(Point.count)
#
#
# # class Robot:
# #     k = 0
# #
# #     def __init__(self, name):
# #         self.name = name
# #         print("Инициализация робота:", self.name)
# #         Robot.k += 1
# #
# #     def __del__(self):
# #         print(self.name, "выключается!")
# #         Robot.k -= 1
# #
# #         if Robot.k == 0:
# #             print(self.name, "был последним")
# #         else:
# #             print("Работающих роботов осталось:", Robot.k)
# #
# #     def say_hi(self):
# #         print("Приветствую! Меня зовут:", self.name)
# #
# #
# # droid1 = Robot("R2-D2")
# # droid1.say_hi()
# # print("Численность роботов:", Robot.k)
# #
# # droid2 = Robot("C-3PO")
# # droid2.say_hi()
# # print("Численность роботов:", Robot.k)
# #
# # droid3 = Robot("PC-3O")
# # droid3.say_hi()
# # print("Численность роботов:", Robot.k)
# #
# # print("\nЗдесь роботы могут проделать какую-то работу\n")
# # print("Роботы закончили свою работу. Давайте их выключим.")
# #
# # del droid1
# # del droid2
# # del droid3
# #
# # print("Численность роботов:", Robot.k)
#
#
# # class Point:
# #
# #     def __init__(self, x, y):
# #         self.__x = self.__y = 0
# #         if Point.__check_value(x) and Point.__check_value(y):
# #             self.__x = x
# #             self.__y = y
# #
# #     def __check_value(s):
# #         if isinstance(s, int) or isinstance(s, float):
# #             return True
# #         return False
# #
# #     def set_coord(self, x, y):
# #         if Point.__check_value(x) and Point.__check_value(y):
# #             self.__x = x
# #             self.__y = y
# #         else:
# #             print("Координаты должны быть числами")
# #
# #     def set_coord_x(self, x):
# #         if Point.__check_value(x):
# #             self.__x = x
# #         else:
# #             print("Координаты должны быть числами")
# #
# #     def set_coord_y(self, y):
# #         if Point.__check_value(y):
# #             self.__y = y
# #         else:
# #             print("Координаты должны быть числами")
# #
# #     def get_coord(self):
# #         return self.__x, self.__y
# #
# #     def get_coord_x(self):
# #         return self.__x
# #
# #     def get_coord_y(self):
# #         return self.__y
# #
# #
# # p1 = Point(5, "10")
# # # print(p1.__dict__)
# # # p1.z = 20
# # # print(p1.__x, p1.__y)
# # # p1.__x = 50
# # # p1.__y = "abc"
# # p1.set_coord(5.2, 100)
# # print(p1.get_coord())
# # p1.set_coord_x(10)
# # p1.set_coord_y(50)
# #
# # p1._Point__x = "abc"
# # # print(p1._Point__x)
# # print(p1.__dict__)
#
# # import os
# # import time
# #
# # file_path = "nested1\\nested2\\test3.txt"
# #
# # if os.path.exists(file_path):
# #     directory, name = os.path.split(file_path)
# #     atime = os.path.getatime(file_path)
# #     t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))
# #     print(f"{name} ({directory}) - время последнего доступа к файлу {t}")
# # else:
# # #     print(f"Файл {file_path} не существует")
#
#
#
# # class MixinLog:
# #     ID = 0
# #
# #     def __init__(self):
# #         print("Init MixinLog")
# #         MixinLog.ID += 1
# #         self.id = MixinLog.ID
# #
# #     def save_sell_log(self):
# #         print(f"{self.id}: товар был продан в 17:15")
# #
# #
# # class Goods:
# #     def __init__(self, name, weight, price):
# #         print("Init Goods")
# #         self.name = name
# #         self.weight = weight
# #         self.price = price
# #         super().__init__()
# #
# #     def print_info(self):
# #         print(f"{self.name}, {self.weight}, {self.price}")
# #
# #
# # class Notebook(Goods, MixinLog):
# #     pass
# #
# #
# # n = Notebook("HP", 1.5, 35000)
# # n.print_info()
# # n.save_sell_log()
#
# #
# # class Account:
# #     rate_usd = 0.013
# #     rate_eur = 0.011
# #     suffix = "RUB"
# #     suffix_usd = "USD"
# #     suffix_eur = "EUR"
# #
# #     def __init__(self, num, surname, percent, value):
# #         self.__num = num
# #         self.__surname = surname
# #         self.__percent = percent
# #         self.__value = value
# #         print(f"Счёт #{self.__num} принадлежащий {self.__surname} был открыт.")
# #         print("*" * 50)
# #
# #     def __del__(self):
# #         print("*" * 50)
# #         print(f"Счёт #{self.__num} принадлежащий {self.__surname} был закрыт.")
# #
# #     @staticmethod
# #     def convert(value, rate):
# #         return value * rate
# #
# #     @classmethod
# #     def set_usd_rate(cls, rate):
# #         cls.rate_usd = rate
# #
# #     @classmethod
# #     def set_eur_rate(cls, rate):
# #         cls.rate_eur = rate
# #
# #     @property
# #     def change_num(self):
# #         return self.__num
# #
# #     @change_num.setter
# #     def change_num(self, n):
# #         self.__num = n
# #
# #     @property
# #     def change_surname(self):
# #         return self.__surname
# #
# #     @change_surname.setter
# #     def change_surname(self, name):
# #         self.__surname = name
# #
# #     @property
# #     def change_percent(self):
# #         return self.__percent
# #
# #     @change_percent.setter
# #     def change_percent(self, percents):
# #         self.__percent = percents
# #
# #     @property
# #     def change_value(self):
# #         return self.__value
# #
# #     @change_value.setter
# #     def change_value(self, val):
# #         self.__value = val
# #
# #     def convert_to_usd(self):
# #         usd_val = Account.convert(self.__value, Account.rate_usd)
# #         print(f"Состояние счёта: {usd_val} {Account.suffix_usd}")
# #
# #     def convert_to_eur(self):
# #         eur_val = Account.convert(self.__value, Account.rate_eur)
# #         print(f"Состояние счёта: {eur_val} {Account.suffix_eur}")
# #
# #     def print_balance(self):
# #         print(f"Текущий баланс {self.__value} {Account.suffix}")
# #
# #     def print_info(self):
# #         print("Информация о счёте: ")
# #         print("-" * 20)
# #         print(f"#{self.__num}")
# #         print(f"Владелец: {self.__surname}")
# #         self.print_balance()
# #         print(f"Проценты: {self.__percent:.0%}")
# #         print("-" * 20)
# #
# #     def edit_owner(self, surname):
# #         self.__surname = surname
# #
# #     def add_percents(self):
# #         self.__value += self.__value * self.__percent
# #         print("Проценты были успешно начислены")
# #         self.print_balance()
# #
# #     def withdraw_money(self, val):
# #         if val > self.__value:
# #             print(f"К сожалению у вас нет {val} {Account.suffix}")
# #         else:
# #             self.__value -= val
# #             print(f"{val} {Account.suffix} было успешно снято")
# #             self.print_balance()
# #
# #     def add_money(self, val):
# #         self.__value += val
# #         print(f"{val} {Account.suffix}, было успешно добавлено!")
# #         self.print_balance()
# #
# #
# #
# #
# # acc = Account("12345", "Долгих", 0.03, 1000)
# # # acc.print_balance()
# # acc. print_info()
# # acc.convert_to_usd()
# # acc.convert_to_eur()
# # print()
# #
# # Account.set_usd_rate(2)
# # acc.convert_to_usd()
# # Account.set_eur_rate(3)
# # acc.convert_to_eur()
# #
# # acc.edit_owner("Дюма")
# # acc.print_info()
# # print()
# #
# # acc.add_percents()
# # print()
# #
# # acc.withdraw_money(100)
# # print()
# #
# # acc.withdraw_money(3000)
# # print()
# #
# # acc.withdraw_money(8000)
# # print()
# #
# # acc.add_money(5000)
# # print()
# #
# # acc.add_money(9000)
# # print()
# #
# # acc.withdraw_money(3000)
# # print()
#
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

import math


class Point:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(x * x + y * y)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


p1 = Point(10, 20)
# p1.z = 30
# print(p1.__dict__)

print(p1.length)