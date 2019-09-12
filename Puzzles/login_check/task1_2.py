# 1. Создать программу, которая будет проверять корректность ввода логина.
# Корректным логином будет строка от 2-х до 10-ти символов, содержащая только буквы или цифры,
# и при этом цифра не может быть первой.
# а) без использования регулярных выражений;
# б) с использованием регулярных выражений.


import re


def descr():
    return "Проверка введенного логина (regexp)."


def run():
    login = input("Enter login: ")
    print("Correct Login" if re.search("^[a-zA-Z][a-zA-Z\d]{1,9}$", login) else "Incorrect Login")