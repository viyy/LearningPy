import random


class Doubler2:
    def __init__(self):
        self._move_count = 0
        self._history = []
        self._current = 1
        self._finish = random.randint(20, 100)
        self._lose = False
        self._win = False
        self.__solve()

    def __solve(self):
        self._need = 0
        tc = self._finish
        while tc > 1:
            if tc % 2 == 1:
                tc -= 1
            else:
                tc /= 2
            self._need += 1

    def plus_one(self):
        if self._win or self._lose:
            return
        self._current += 1
        self._history.append("+")
        self._move_count += 1
        self.check()

    def check(self):
        if self._current > self._finish:
            self._lose = True
            self._win = False
        elif self._current == self._finish:
            self._lose = False
            self._win = True

    def double(self):
        if self._win or self._lose:
            return
        self._current *= 2
        self._history.append("*")
        self._move_count += 1
        self.check()

    def reset(self):
        self._current = 1
        self._history = []
        self._win = False
        self._lose = False

    def undo(self):
        if self._history[-1] == "+":
            self._current -= 1
        else:
            self._current = int(self._current / 2)
        self._history.pop()

    @property
    def current(self):
        return self._current

    @property
    def finish(self):
        return self._finish

    @property
    def state(self):
        if self._win:
            return 1
        if self._lose:
            return -1
        return 0

    @property
    def move_count(self):
        return self._move_count

    @property
    def need_turns(self):
        return self._need
