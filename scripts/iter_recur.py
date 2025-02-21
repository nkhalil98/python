# two positive integers multiplication
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


def mult_recur(a, b):
    if b == 1:
        return a
    else:
        return a + mult_recur(a, b - 1)


# calculating factorial
def factorial_iter(n):
    result = 1
    if n == 1 or n == 0:
        return result

    while n > 0:
        result *= n
        n -= 1
    return result


def factorial_recur(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recur(n - 1)


# multiply elements of a list
def mult_list_iter(L):
    if len(L) == 0:
        return
    prod = 1
    for e in L:
        prod *= e
    return prod


def mult_list_recur(L):
    if len(L) == 0:
        return
    if len(L) == 1:
        return L[0]
    return L[0] * mult_list_recur(L[1:])


# find if element is in an ordered list
def find_elem_iter(L, e):
    if len(L) == 0:
        return False
    for element in L:
        if element == e:
            return True
    return False


def find_elem_recur(L, e):
    if len(L) == 0:
        return False
    if len(L) == 1:
        return L[0] == e
    mid = len(L) // 2
    if L[mid] > e:
        return find_elem_recur(L[:mid], e)
    else:
        return find_elem_recur(L[mid:], e)
