from colorama import init, Fore, Back, Style
from Puzzles.loginCheck import task1_1, task1_2
from Puzzles.words_in_message import task2
from Puzzles.string_trace import task3
from Puzzles.pairs import task4

init()

puzzles = [[task1_1.descr, task1_1.run],
           [task1_2.descr, task1_2.run],
           [task2.descr, task2.run],
           [task3.descr, task3.run],
           [task4.descr, task4.run]]
i = -1
while i != 0:
    for x in range(0, len(puzzles)):
        print("[{}] - ".format(x+1)+puzzles[x][0]())
    else:
        print(Fore.RED + "[0] - Exit")
        i = input(Fore.GREEN + "Method to run->")
        if i.isdecimal():
            i = int(i)
            if 0 < int(i) <= len(puzzles):
                print("\n" + Fore.CYAN + Style.BRIGHT + "---------- Run Puzzle #{} ----------".format(i) + Style.RESET_ALL)
                puzzles[int(i)-1][1]()
                print(Fore.CYAN + Style.BRIGHT + "---------- End of Puzzle ----------" + "\n" + Style.RESET_ALL)
