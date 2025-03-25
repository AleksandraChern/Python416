

import re

a = input("Введите адрес электронной почты. ")
print(a)

s = "123456@i.ru 123_456@ru.name.ru login@i.ru логин-1@i.ru login.3@i.ru login.3-67@i.ru 1login@ru.name.ru"
reg = r"\w[A-Za-zа-я0-9_.+-]+@[A-Za-zа-я0-9]+\.[A-Za-zа-я0-9]"

print(re.split(r"\s", s))
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"[а-яa-zA-Z0-9_.]{1-9}", login)
#
# print(validate_login("123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"))
# print(validate_login())
