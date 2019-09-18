from colorama import init, Fore, Style

from Puzzles.doubler import task5
from Puzzles.ege import task7
from Puzzles.hard_ege import task9
from Puzzles.login_check import task1_1, task1_2
from Puzzles.pairs import task4
from Puzzles.string_trace import task3
from Puzzles.tel import task8
from Puzzles.words_in_message import task2
from Puzzles.believe_or_not import task6

init()

puzzles = [[task1_1.descr, task1_1.run],
           [task1_2.descr, task1_2.run],
           [task2.descr, task2.run],
           [task3.descr, task3.run],
           [task4.descr, task4.run],
           [task5.descr, task5.run],
           [task6.descr, task6.run],
           [task7.descr, task7.run],
           [task8.descr, task8.run],
           [task9.descr, task9.run]]
i = -1
while i != 0:
    for x in range(0, len(puzzles)):
        print("[{}] - ".format(x+1)+puzzles[x][0]())
    else:
        print(Fore.RED + Style.BRIGHT + "[0] - Exit" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT)
        i = input("Puzzle to run->")
        if i.isdecimal():
            i = int(i)
            if 0 < int(i) <= len(puzzles):
                print("\n" + Fore.CYAN + Style.BRIGHT + "---------- Run Puzzle #{} ----------".format(i) + Style.RESET_ALL)
                puzzles[int(i)-1][1]()
                print(Fore.CYAN + Style.BRIGHT + "---------- End of Puzzle ----------" + "\n" + Style.RESET_ALL)
