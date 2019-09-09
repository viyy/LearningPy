# 3. Для двух строк написать метод, определяющий, является ли одна строка перестановкой другой.
# Регистр можно не учитывать.
# Например:
# badc являются перестановкой abcd


def descr():
    return "{} - Проверка строк на перестановку"


def calculate_trace(inp):
    path = {}
    for c in inp.lower():
        path[c] = path[c] + 1 if c in path else 1
    return path


def run():
    str1 = input("Enter 1st string: ")
    str2 = input("Enter 2nd string: ")
    trace1 = calculate_trace(str1)
    trace2 = calculate_trace(str2)
    flag = True
    if len(trace1) == len(trace2):
        for k, v in trace1.items():
            if k not in trace2 or trace2[k] != v:
                flag = False
                break
    else:
        flag = False
    print("String \"" + str1 + "\" is " + ("" if flag else "not ") + "recombination of string \"" + str2 + "\"")
