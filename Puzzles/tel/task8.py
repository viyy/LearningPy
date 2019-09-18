import re


def descr():
    return "Поиск телефонов"


def run():
    text = open("Puzzles/tel/Text.txt", "r").read()
    res = re.findall(r"\d{2}-\d{2}-\d{2}|\d{3}-\d{3}|\d{3}-\d{2}-\d{2}", text)
    print(res)
