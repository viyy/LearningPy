import datetime
import os
import random
import struct

__COUNT = 10000000
__MinValue = 0
__MaxValue = 100000
__STOP = False


def generate(path):
    t = []
    with open(path, "wb") as f:
        for i in range(__COUNT):
            t.append(int(__MinValue + (__MaxValue - __MinValue) * random.random()))
        f.write(struct.pack('%si' % len(t), *t))


def descr():
    return "Работа с бинарными файлами"


def calculate(path):
    max1 = -1
    max2 = -1
    pos1 = 0
    max3 = -1
    cur_pos = 0
    available = os.path.getsize(path)
    with open(path, "rb") as f:
        while cur_pos < available:
            tp = cur_pos
            t, = struct.unpack('i', f.read(4))
            cur_pos += 4
            if t <= max1:
                continue
            max1 = t
            pos1 = tp
        f.seek(pos1 + 8 * 4, 0)
        cur_pos = pos1 + 8 * 4
        while cur_pos < available:
            t, = struct.unpack('i', f.read(4))
            cur_pos += 4
            if t <= max2:
                continue
            max2 = t
        f.seek(0, 0)
        cur_pos = 0
        while cur_pos < pos1 - 8 * 4:
            t, = struct.unpack('i', f.read(4))
            cur_pos += 4
            if t <= max2:
                continue
            max2 = t
        f.seek(pos1 - 8 * 4, 0)
        cur_pos = pos1 - 8 * 4
        a = []
        for i in range(17):
            a.append(struct.unpack('i', f.read(4))[0])
            cur_pos += 4
        for i in range(8):
            for j in range(i+9, 17):
                t = a[i] * a[j]
                if t > max3:
                    max3 = t
        max1 = max1 * max2
        return max3 if max3 > max1 else max1


def run():
    print("Generate...")
    t = datetime.datetime.now()
    generate("test.bin")
    t1 = datetime.datetime.now()
    print("Generated in {}".format((t1 - t)))
    print("Search...")
    t = datetime.datetime.now()
    res = calculate("test.bin")
    t1 = datetime.datetime.now()
    print("Calculated in {}".format((t1 - t)))
    print("Answer: {}".format(res))
