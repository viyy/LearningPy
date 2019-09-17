def list_to_string(arr):
    res = ""
    for x in arr:
        res += "{} ".format(x)
    res = res.strip()
    return res


def take(arr, count):
    if count > len(arr):
        return []
    res = []
    for i in range(count):
        res.append(arr[i])
    return res


def distinct(arr, key):
    res = []
    for x in arr:
        if key(x) in res:
            continue
        res.append(x)
    return res
