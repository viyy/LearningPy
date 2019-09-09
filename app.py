from Puzzles.loginCheck import task1_1, task1_2
from Puzzles.words_in_message import task2
from Puzzles.string_trace import task3

puzzles = [[task1_1.descr, task1_1.run],
           [task1_2.descr, task1_2.run],
           [task2.descr, task2.run],
           [task3.descr, task3.run]]
i = -1
while i != 0:
    for x in range(0, len(puzzles)):
        print(puzzles[x][0]().format(x+1))
    else:
        print("0 - Exit")
        i = input("Method to run->")
        if i.isdigit():
            i = int(i)
            if 0 < int(i) <= len(puzzles):
                print("----Run Puzzle #{}----".format(i))
                puzzles[int(i)-1][1]()
                print("----End of Puzzle----")
