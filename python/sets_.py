# set creation
# ------------
set1 = {1, 2, 3}
set2 = set([3, 4, 5])  # from iterable
empty = set()  # the only way to initilize an empty set
fset = frozenset({1, 2, 3, 4, 5})  # frozenset (immutable set)
fset2 = frozenset([6, 7, 8])  # from iterable


# set operations
# --------------
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b  # {1, 2, 3, 4, 5}
intersection = a & b  # {3}
difference = a - b  # {1, 2}
symmetric_difference = a ^ b  # {1, 2, 4, 5}


# set methods
# -----------
s = {1, 2, 3}
s.add(4)
s.update([5, 6, 7])
s.remove(7)  # raises KeyError if not found
s.discard(8)  # does not raise error if not found
popped = s.pop()  # remove and return an arbitrary element
s.clear()  # remove all elements


# sets are containers
# -------------------
s = {1, 2, 3, 4, 5}
length = len(s)
has_one = 1 in s  # True
has_ten = 10 in s  # False


# comparing sets
# --------------
a.issubset(b)  # equivalent to a <= b
a.issuperset(b)  # equivalent to a >= b
a == b


# set comprehensions
# ------------------

L = [1, 2, 3, 2, 1, 4, 5, 3]
unique_squares = {x**2 for x in L}  # {1, 4, 9, 16, 25}


# Checking for duplicates
# -----------------------


def has_duplicates_no_set(seq):  # slow
    seen = []
    for item in seq:
        if item in seen:
            return True
        seen.append(item)
    return False


def has_duplicates_with_set(seq):  # fast
    return len(set(seq)) < len(seq)
