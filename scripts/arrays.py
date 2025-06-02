def rotate(arr, direction, shift):
    shift = shift % len(arr)
    if direction == "right":
        return arr[-shift:] + arr[:-shift]
    elif direction == "left":
        return arr[shift:] + arr[:shift]


def insert_element(arr, e, n):
    out = []
    for i in range(len(arr)):
        out.append(arr[i])
        if (i + 1) % n == 0:
            out.append(e)
    return out


def insert_element_inplace(arr, e, n):
    ptr = 0
    while ptr + n < len(arr):
        ptr += n
        arr.insert(ptr, e)
        ptr += 1
    return arr


def chunck(arr, n):
    result = [arr[i : i + n] for i in range(0, len(arr), n)]
    return result
