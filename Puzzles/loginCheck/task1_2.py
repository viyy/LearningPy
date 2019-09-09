import re


def descr():
    return "{} - Проверка введенного логина (regexp)."


def run():
    login = input("Enter login: ")
    print("Correct Login" if re.search("^[a-zA-Z][a-zA-Z\d]{1,9}$", login) else "Incorrect Login")
