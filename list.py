# python lists are dynamic arrays
# lookup by index is O(1)
# lookup by value is O(n)
# inserting or deleting an element is O(n)
# appending an element is O(1)
# python lists can store multiple types of data

my_list = [1, 2, 'three', [4, 5, 6], True]
my_list.append(5)

# to make a shallow copy of the list:
copy_1 = list(my_list)
copy_2 = my_list[:]
copy_3 = my_list.copy()

# to make a deep copy of the list:
import copy
deep_copy = copy.deepcopy(my_list)