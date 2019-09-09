# 1. Создать программу, которая будет проверять корректность ввода логина.
# Корректным логином будет строка от 2-х до 10-ти символов, содержащая только буквы или цифры,
# и при этом цифра не может быть первой.
# а) без использования регулярных выражений;
# б) с использованием регулярных выражений.


def descr():
    return "{} - Проверка введенного логина."


def run():
    login = input("Enter login: ")
    if len(login) < 2 or len(login) > 10:
        return print("Incorrect login")
    if not login.isalnum():
        return print("Incorrect login")
    if login[0].isdigit():
        return print("Incorrect login")
    print("Correct login")
