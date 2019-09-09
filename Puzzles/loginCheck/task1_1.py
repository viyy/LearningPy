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
