import random


class Doubler:
    def __init__(self):
        self._current = 1
        self._finish = random.randint(20, 100)
        self._lose = False
        self._win = False

    def plus_one(self):
        if self._win or self._lose:
            return
        self._current += 1
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
        self.check()

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
