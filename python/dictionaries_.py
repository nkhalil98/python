from collections import defaultdict, OrderedDict, Counter, UserDict, ChainMap

# TODO: chainmap
# TODO: userdict example

# dictionary creation
# -------------------

# dictionaries are key-value pairs where keys are unique and hashable
# dictionaries are hash tables

# dictionary literal
my_dict = {"a": 2, "b": 1, "c": 3}
empty = {}  # initilize an empty dict
empty2 = dict()  # initialize an empty dict

## accessing, adding, updating, and deleting items
a = my_dict["a"]  # access value by key
# z = my_dict["z"]  # KeyError if key not found
my_dict["d"] = 4  # add a new key-value pair
my_dict["a"] = 0  # update the value of an existing key
del my_dict["b"]  # delete a key-value pair


# dictionary methods
# ------------------
my_dict = {"a": 2, "b": 1, "c": 3}
keys_ = list(my_dict.keys())  # list of keys
vals_ = list(my_dict.values())  # list of values
items_ = list(my_dict.items())  # list of (key, value) tuples
z = my_dict.get("z")  # 0  safely get value by key, returns None if key not found
a = my_dict.pop("a")  # remove and return the value of "a"
my_dict.clear()  # clear all items
my_dict2 = {"e": 5}
my_dict.update(my_dict2)  # merge dictionaries


# dictionaries are a collection type
# ----------------------------------
n = len(my_dict)  # number of key-value pairs
has_x = "x" in my_dict  # check if key exists


# iterating over dictionaries
# ---------------------------

## iterte over keys
for key in my_dict:
    print(key, my_dict[key])

for key in my_dict.keys():
    print(key, my_dict[key])

## iterate over values
for value in my_dict.values():
    print(value)

## iterate over items
for key, value in my_dict.items():
    print(key, value)

## using sorted() to iterate in a specific order
for key, value in sorted(my_dict.items(), key=lambda x: x[1]):
    print(key, value)


# dictionary comprehensions
# -------------------------

nums = [1, 2, 3]
squares = [x**2 for x in nums]
square_map = {k: v for k, v in zip(nums, squares)}
cube_map = {x: x**3 for x in nums}


# Counter
# -------

my_string = "hello word"

# counter 1
counter1 = Counter(my_string)

cnt_o_1 = counter1["o"]  # 2
cnt_a_1 = counter1["a"]  # 0 (does not return None or throws an error)

# counter 2
counter2 = {}
for char in my_string:
    if char not in counter2:
        counter2[char] = 1
    else:
        counter2[char] += 1

cnt_o_2 = counter2["o"]  # 2

# counter 3
counter3 = {}

for char in my_string:
    counter3[char] = counter3.get(char, 0) + 1

cnt_o_3 = counter3["o"]  # 2

# Counter operations
s = "hello world"
t = "hello python"
word_count = Counter(s)
word_count2 = Counter(t)
cnt_e = word_count["e"]  # 1
cnt_a = word_count["a"]  # 0 (does not return None or throws an error)
most_common = word_count.most_common()
all_counts = word_count + word_count2


# defaultdict
# -----------

d = defaultdict(list)
d["a"].append(1)
d["b"].append(2)
d["a"].append(3)


# OrderedDict
# ------------

# maintains the insertion order of keys. has methods that are useful for
# implementing caches like LRU (least recently used) cache

od = OrderedDict()
od["b"] = 2
od["a"] = 1
od["c"] = 3

for key, value in od.items():
    print(key, value)

od.popitem(last=False)  # removes the first item
od.move_to_end("a")  # moves key "a" to the end
od.move_to_end("a", last=False)  # moves key "a" to the beginning
