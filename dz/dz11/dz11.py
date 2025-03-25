

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
print("Искомыми буквами являются: ")
c = set(a) - set(b)

for i in c:
    print(i, end=" ")



