

a = [int(input("-> ")) for i in range(int(input("n = ")))]
s = 0
for i in range(len(a)):
    if a[i] < 0:
        s += a[i]
print("Сумма отрицательных элементов:", s)
