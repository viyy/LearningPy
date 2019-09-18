class List:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        if not hasattr(arr, "__iter__"):
            raise TypeError(
                u"Enumerable must be instantiated with an iterable object"
            )
        self.__list = arr

    def distinct(self, key):
        res = []
        keys = []
        for x in self.__list:
            if key(x) in keys:
                continue
            res.append(x)
            keys.append(key(x))
        return List(res)

    def take(self, count):
        if count > len(self.__list):
            return List()
        res = []
        for i in range(count):
            res.append(self.__list[i])
        return List(res)

    def __iter__(self):
        cache = []
        for element in self.__list:
            cache.append(element)
            yield element
        self.__list = cache

    def count(self):
        return len(self.__list)

    def select(self, func=lambda x: x):
        res = []
        for element in self.__list:
            res.append(func(element))
        return List(res)

    def to_array(self):
        res = []
        for el in self.__list:
            res.append(el)
        return res

    def first(self):
        return self.__list[0] if self.count() > 0 else None

    def sort(self, key=lambda x: x):
        self.__list.sort(key=key)
        return self

    def __add__(self, other):
        self.__list.append(other)

    def __contains__(self, item):
        return item in self.__list

    def add(self, other):
        self.__list.append(other)

    def contains(self, item):
        return item in self.__list

    def __str__(self):
        return ', '.join(map(str, self.__list))
