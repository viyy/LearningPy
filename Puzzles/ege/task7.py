import datetime

from Puzzles.ege.Student import Student
from my_utils.List import List

__students = List()
__worse = List()


def descr():
    return "Задача ЕГЭ"


def load(path):
    global __students
    f = open(path, "r")
    n = int(f.readline())
    for i in range(n):
        data = f.readline()
        __students.add(Student(data))
    f.close()


def calculate_worse():
    global __students
    global __worse
    __worse = __students.sort(lambda x: x.points).distinct(lambda x: x.points).take(3).select(lambda x: x.points)


def run():
    t = datetime.datetime.now()
    load("Puzzles/ege/data.txt")
    t1 = datetime.datetime.now()
    print("Loaded in {}".format((t1-t)))
    t = datetime.datetime.now()
    calculate_worse()
    t1 = datetime.datetime.now()
    print("Worse points calculated in {}".format((t1 - t)))
    print("Worse points: {}".format(__worse))
    t = datetime.datetime.now()
    for s in __students:
        if s.points in __worse:
            print(s.to_string())
    t1 = datetime.datetime.now()
    print("Check complete in {}".format((t1 - t)))
