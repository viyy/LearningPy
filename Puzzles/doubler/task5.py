from Puzzles.doubler.doubler import Doubler


def descr():
    return "Удвоитель"


def skip():
    pass


def run():
    d = Doubler()
    i = -1
    while d.state == 0 and i != 0:
        print("--- Next turn ---")
        print("Current: {}".format(d.current))
        print("Target:  {}".format(d.finish))
        print("[1] +1\n[2] *2\n[3] reset\n[0] exit")
        i = input("Action? ->")
        i = int(i) if i.isdigit() else -1
        _ = {1: d.plus_one,
             2: d.double,
             3: d.reset}.get(i, skip)()
        if d.state == 1:
            print("You win!!!")
        if d.state == -1:
            print("You lose!!!")
