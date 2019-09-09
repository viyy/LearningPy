separators = [".", ",", ":", ";", " ", "!", "?"]


def descr():
    return "{} - Простой анализ сообщения"


def only_short(msg, n):
    res = ""
    tmp = ""
    word_len = 0
    for c in msg:
        if c not in separators:
            word_len += 1
            tmp += c
        else:
            if word_len <= n:
                res += tmp + c
            tmp = ""
            word_len = 0
    return res


def del_with_last_char(msg, char):
    res = ""
    tmp = ""
    for c in msg:
        if c not in separators:
            tmp += c
        else:
            if len(tmp) > 0 and tmp[len(tmp)-1] != char:
                res += tmp
            res += c
            tmp = ""
    return res


def get_longest_word(msg):
    res = ""
    tmp = ""
    max_len = 0
    word_len = 0
    for c in msg:
        if c not in separators:
            word_len += 1
            tmp += c
        else:
            if word_len > max_len:
                res = tmp
                max_len = word_len
            tmp = ""
            word_len = 0
    return res


def get_all_longest_words(msg):
    res = []
    tmp = ""
    max_len = 0
    word_len = 0
    for c in msg:
        if c not in separators:
            word_len += 1
            tmp += c
        else:
            if word_len == max_len:
                res.append(tmp)
            if word_len > max_len:
                res = [tmp]
                max_len = word_len
            tmp = ""
            word_len = 0
    return res


def run():
    msg = open("Puzzles/words_in_message/message.txt", "r").read()
    n = "a"
    while not n.isdigit():
        n = input("Enter max word length: ")
    else:
        n = int(n)
        x = input("Enter the last character of the words to be deleted: ")
        print("--Only words shorter than {}".format(n))
        print(only_short(msg, n))
        print("--Deleted words with last char \"" + x + "\"")
        print(del_with_last_char(msg, x))
        print("--Longest word")
        print(get_longest_word(msg))
        print("--All longest words")
        print(get_all_longest_words(msg))
