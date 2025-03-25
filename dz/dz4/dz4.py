

a = int(input("Укажите количество символов: "))
sign = input("Тип символов: ")
position = int(input("0 - горизонтальная\n1 - вертикальная \nориентация линии: "))
b = 0
while b < a:
    if position == 1:
        print(sign)
    else:
        print(sign, end=" ")
    b += 1


