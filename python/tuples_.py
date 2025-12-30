from collections import namedtuple


# tuple creation
# --------------

tup = (1, 2, 3)
tup2 = 4, 5, 6  # tuples do not require parentheses
t = 1,  #  single element tuple requires a trailing comma # fmt: skip
empty = ()  # initialize an empty tuple
empty = tuple()  # initialize an empty tuple


# tuples are sequences
# --------------------

tup = (1, 2, 3, 4, 5)

## length
length = len(tup)

## indexing and slicing
first = tup[0]  # indexing
last = tup[-1]  # negative indexing
subtuple = tup[1:4]  # slicing

## concatenation
tup2 = tup + (6, 7, 8)

## repetition
doubled = tup * 2

## membership (in operator)
has_3 = 3 in tup  # True
has_9 = 9 in tup  # False

## tuples are immutable
# tup[0] = 4  # TypeError: 'tuple' object does not support item assignment
new_tup = (0,) + tup  # creates a new tuple


# tuple methods
# -------------
tup = (1, 2, 3, 2, 4, 2)
count_2 = tup.count(2)  # 3
index_3 = tup.index(3)  # 2


# comparing tuples
# ----------------

# element-wise comparison
(1,) > (0,)  # True
(1, 2) > (1, 3)  # False
(1, 2, 3) > (1, 2, 3, 4)  # False


# tuples with variables
# ---------------------
x, y = 10, 20  # multiple assignment
x, y = y, x  # swap values


## function multiple return values
def min_max(nums: list[int]) -> tuple[int, int]:
    return min(nums), max(nums)  # returns a tuple


min_max_tup = min_max([3, 1, 4, 1, 5, 9])


# tuple unpacking
# ---------------

## basic unpacking
tup = (1, 2, 3)
tup2 = (1, 2, 3, 4, 5)
x, y, z = tup  # multiple assignment is tuple unpacking
x, y, *rest = tup2  # advanced unpacking with rest (rest is a list)
x, y, *_ = tup2  # rest can be empty
# x, y = tup2  throws ValueError: too many values to unpack (expected 2, got 5)

## unpacking and packing in function arguments

### unpacking
names = ("Alice", "Bob", "Charlie")
print(*names)  # tuple unpacking using the * operator

nums = (3, 2)
print(divmod(*nums))  # unpacking arguments


### argument packing
def mean(*args):  # args is a tuple
    return sum(args) / len(args) if args else 0


# enumerate
# ---------

arr = list("abcd")
for index, char in enumerate(arr):
    print(index, char)


# zip
# ---

# if the lengths of the iterables do not match, the result will be truncated to
# the length of the shortest iterable
X = [1, 2, 3]
Y = [4, 5, 6]

for x, y in zip(X, Y):
    print(x, y)

## list from zip
coordinates = list(zip(X, Y))

## dict from zip
coordinate_dict = dict(zip(X, Y))
coordinate_dict2 = {x: y for x, y in zip(X, Y)}


# namedtuple
# ----------

# named tuples are like regular tuples but with named fields for better
# readability and access

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
x_coord = p.x
y_coord = p.y
# p.x = 30  # AttributeError: can't set attribute (namedtuples are immutable)
