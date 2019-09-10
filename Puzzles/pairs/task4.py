import random
from my_utils import list_utils

min_val = -10000
max_val = 10000
arr_len = 5
array = []


def descr():
    return "Поиск пар элементов, в которых есть число, кратное 3"


def init_array():
    global array
    array = []
    for i in range(arr_len):
        array.append(random.randint(min_val, max_val))


def run():
    init_array()
    print("Initial array:")
    print(list_utils.list_to_string(array))
    c = 0
    if len(array) - 1 <= 0:
        return print("Answer: 0")
    l: int = len(array)
    for x in range(l-1):
        if array[x] % 3 == 0 or array[x+1] % 3 == 0:
            c += 1
    print("--Answer: {}".format(c))
