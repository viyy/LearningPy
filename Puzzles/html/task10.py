import re
from os import walk


__PATH = "Puzzles/html/demo"
regex = r"<img src=\"([\w\d\\\\.\/а-яА-Я\-]+)\" "


def descr():
    return "Поиск картинок в html"


def run():
    f = []
    res = []
    for (_, _, filenames) in walk(__PATH):
        f.extend(filenames)
        break
    for file in f:
        if file[-5:] != '.html':
            continue
        fh = open(__PATH + '/' + file, "r", encoding="UTF-8")
        data = fh.read()
        fh.close()
        res.extend(re.findall(regex, data))
    print(res)
