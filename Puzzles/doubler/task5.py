from Puzzles.doubler.doubler import Doubler
from my_utils.console_utils import clear


def descr():
    return "Удвоитель"


def run():
    d = Doubler()
    i = -1
    while d.state == 0 and i != 0:
        clear()
        print("--- Next turn ---")
        print("Current: {}".format(d.current))
        print("Target:  {}".format(d.finish))
        print("[1] +1\n[2] *2\n[0] exit")
        i = input("Action? ->")
        i = int(i) if i.isdigit() else -1
        if i == 1:
            d.plus_one()
        if i == 2:
            d.double()
        if d.state == 1:
            print("You win!!!")
        if d.state == -1:
            print("You lose!!!")
