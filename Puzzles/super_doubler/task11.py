from Puzzles.super_doubler.Doubler2 import Doubler2


def descr():
    return "Удвоитель+"


def skip():
    pass


def run():
    d = Doubler2()
    i = -1
    while d.state == 0 and i != 0:
        print("--- Next turn ---")
        print(f"Current: {d.current:4}    Target: {d.finish:4}")
        print(f"Perfect: {d.need_turns:4}    Score: {d.move_count:5}")
        print("[1] +1\n[2] *2\n[3] undo\n[4] reset\n[0] exit")
        i = input("Action? ->")
        i = int(i) if i.isdigit() else -1
        _ = {1: d.plus_one,
             2: d.double,
             3: d.undo,
             4: d.reset}.get(i, skip)()
        if d.state == 1:
            print("You win!!!")
        if d.state == -1:
            print("You lose!!!")
