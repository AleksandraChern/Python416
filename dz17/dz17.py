

# w = "I am learning Python. hello, world!"
w = input("Введите строку: ")


a = w[:w.find('h')]
b = w[w.find('h'):w.rfind('h') + 1]
c = w[w.rfind('h') + 1:]
print(a + b[::-1] + c)