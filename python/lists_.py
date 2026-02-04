from copy import deepcopy
from collections import UserList
import array


# list creation
# -------------

# python lists are dynamic arrays of pointers to objects
# python lists can hold items of different types unlike arrays in other
# languages (like C)

my_list = [1, 2, 3, 4, 5]  # list literal
my_list2 = list((1, 2, 3, 4, 5))  # from a sequence (tuple)
my_list3 = list(range(1, 6))  # from a range
my_list4 = [0] * 5  # list with 5 zeros
my_list5 = list("hello")  # from a string (list of characters)
empty = []  # initialize an empty list
empty2 = list()  # another way


# lists are sequences
# -------------------

colors = ["red", "green", "blue"]

## length
length = len(colors)

## indexing and slicing
first = colors[0]  # indexing
last = colors[-1]  # negative indexing
# colors[3]  # IndexError
slice = colors[0:2]  # slicing
reverse_slice = colors[::-1]  # reversing a list

### common slicing patterns
n = 5
a = list(range(100))
first_n = a[:n]
last_n = a[-n:]
all_but_first_n = a[n:]
all_but_last_n = a[:-n]

## concatenation
colors2 = colors + ["yellow", "purple"]

## repetition
repeated_colors = colors * 2

## membership (in operator)
has_red = "red" in colors  # True
has_yellow = "yellow" in colors  # False

## lists are mutable
colors[0] = "crimson"  # modify an item
colors[1:3] = ["lime", "cyan"]  # modify a slice
colors[1:3] = "black"  # TypeError: can only assign an iterable of same length


# iterating over lists
# --------------------
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

for i in range(len(colors)):
    print(colors[i])

for index, color in enumerate(colors):
    print(index, color)

counter = 0
while counter < len(colors):
    print(colors[counter])
    counter += 1


# list methods
# ------------

## adding and removing items
colors = ["red", "green", "blue"]
colors.append("yellow")  # add an item to the end of a list
colors.insert(0, "white")  # insert an item at a specific index
colors.remove("green")  # remove a specific item from a list
colors.pop()  # pop an item from the end of a list
colors.pop(0)  # pop an item from a specific index
del colors[0]  # delete an item at a specific index
colors.extend(
    ["purple", "pink", "orange"]
)  # add multiple items to the end of a list (modifies the list in-place)


## sorting
colors = ["red", "blue", "green"]
colors.sort()  # sort a list in-place
sorted_colors = sorted(colors)  # sort a list in a new list
colors.sort(reverse=True)  # sort a list in reverse order
colors.sort(key=len)  # sort a list by a key function
arr = [("a", 3), ("b", 1), ("n", 2)]
arr.sort(key=lambda x: x[1])  # sort by second item in tuple

## reversing
colors = ["red", "green", "blue"]
colors.reverse()  # reverse the order of a list in-place
reversed_colors = list(reversed(colors))  # reverse the order of a list in a new list

## other methods
colors = ["red", "green", "blue", "red"]
colors.index("blue")  # get the index of a specific item
# colors.index("yellow")  # ValueError if item not found
colors.count("red")  # count the number of occurrences of an item
colors.clear()  # remove all items from a list


# comparing lists
# ----------------

# element-wise comparison
[1] > [0]  # True
[1, 2] > [1, 3]  # False
[1, 2, 3] > [1, 2, 3, 4]  # False
# [1, 2] > [1, "a"]  # TypeError (cannot compare int and str)


# python built-in functions with lists
# ------------------------------------
nums = list(range(1_000_000))
min_ = min(nums)
max_ = max(nums)
sum_ = sum(nums)

arr = [("a", 3), ("b", 1), ("n", 2)]
max_num = max(arr, key=lambda x: x[1])
min_char = min(arr, key=lambda x: x[0])


# list comprehensions
# -------------------

squares = [x**2 for x in range(10)]
squares_and_cubes = [x**2 if x % 2 == 0 else x**3 for x in range(10)]


# aliasing, copying, and deep copying
# -----------------------------------

## aliasing
a = [1, 2, 3]
b = a  # aliasing
b[0] = 4
print(a)  # [4, 2, 3]
print(b)  # [4, 2, 3]
print(b is a)  # True

## copying
a = [1, 2, 3]
b = a.copy()  # shallow copy
c = a[:]  # shallow copy
d = list(a)  # shallow copy
b[0] = 4
c[0] = 5
d[0] = 6
print(a)  # [1, 2, 3]
print(b)  # [4, 2, 3]
print(c)  # [5, 2, 3]
print(d)  # [6, 2, 3]
print(b is a)  # False
print(c is a)  # False
print(d is a)  # False

## deep copy
a = [[1, 2], [3, 4]]
b = a.copy()  # shallow copy
c = deepcopy(a)  # deep copy
b[0][0] = 5
c[1][0] = 6
print(a)  # [[5, 2], [3, 4]]
print(b)  # [[5, 2], [3, 4]]
print(c)  # [[1, 2], [6, 4]]
print(b is a)  # False
print(c is a)  # False


# nested lists
# ------------

## creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

### indexing and slicing
first_row = matrix[0]
first_column = [row[0] for row in matrix]
middle_element = matrix[1][1]

## list containing itself
a = [1, 2, 3]
a.append(a)
print(a)  # [1, 2, 3, [...]]
aa = a[3]
print(aa)  # [1, 2, 3, [...]]
aaa = a[3][3][3][3]  # keeps going deeper forever
print(aaa)  # [1, 2, 3, [...]]


# python list subclassing
# -----------------------
class MyList(UserList):
    def sum(self):
        total = 0
        for item in self.data:
            total += item
        return total

    def product(self):
        result = 1
        for item in self.data:
            result *= item
        return result


my_list = MyList([1, 2, 3, 4, 5])
print(my_list.sum())  # 15
print(my_list.product())  # 120


# array
# -----

arr = array.array("i", [1, 2, 3])  # array of signed integers
arr.append(4)
# arr.append("A")  # TypeError: an integer is required
