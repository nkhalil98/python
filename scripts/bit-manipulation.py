def set_bit(x, position):
    mask = 1 << position
    return x | mask


def clear_bit(x, position):
    mask = 1 << position
    return x & (~mask)


def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask


def is_bit_set(x, position):
    shifted = x >> position
    return shifted & 1


def modify_bit(x, position, state):
    mask = 1 << position
    return (x & mask) | (-state & mask)


def is_even(x):
    return (x & 1) == 0


def is_power_two(x):
    return (x & x - 1) == 0
