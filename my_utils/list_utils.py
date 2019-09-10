def list_to_string(arr):
    res = ""
    for x in arr:
        res += "{} ".format(x)
    res = res.strip()
    return res
