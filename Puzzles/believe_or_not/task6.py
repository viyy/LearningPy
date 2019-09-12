# coding: utf8
import random


__ASK = 5
__YES = u"Да"
__NO = u"Нет"


def descr():
    return "Верю, не верю"


def run():
    score = 0
    questions = []
    nums = []
    strs = open("Puzzles/believe_or_not/q.txt", "r", encoding="utf-8").readlines()
    for s in strs:
        t = s.split("|")
        questions.append([t[0].strip(), t[1].strip()])
    if len(questions) < __ASK:
        return print("Слишком мало вопросов")
    for i in range(__ASK):
        n = random.randrange(0, len(questions))
        if n not in nums:
            nums.append(n)
    for n in nums:
        print(questions[n][0])
        ans = ""
        while ans != "y" and ans != "n":
            ans = input("Ответ (y/n) ->")
            if (ans == "y" and questions[n][1] == __YES) or (ans == "n" and questions[n][1] == __NO):
                score += 1
        print("Правильный ответ: {}".format(questions[n][1]))
    print("\nВаш результат: {}".format(score))
