import itertools

# TODO: itertools module examples

# for loops
# ---------

## range based

### simple range
for i in range(5):
    print(i)  # prints 0, 1, 2, 3, 4

### range with start and stop
for i in range(2, 5):
    print(i)  # prints 2, 3, 4

### range with start, stop, step
for i in range(2, 10, 2):
    print(i)  # prints 2, 4, 6, 8

## iterable based
L = [1, 2, 3, 4, 5]
n = len(L)

### index based
for i in range(n):  # for i in range(n)
    print(L[i])

### reversed index based
for i in range(n - 1, -1, -1):
    print(L[i])

### item based
for item in L:  # for item in iterable
    print(item)

## enumerate
for index, item in enumerate(L):  # for index, item in enumerate(iterable)
    print(f"Index: {index}, Item: {item}")

# the temporary loop variable is not scoped locally to the loop block and can
# overwrite existing variables outside the loop and retain its last value after
# the loop ends
e = 99
print(e)  # prints 99

for e in L:
    pass
print(e)  # prints 5

# we can use _ as a throwaway variable for unused loop variables
for _ in range(3):
    print("Hello")


# while loops
# -----------

## while with a counter
counter = 0
while counter < 10:
    print(counter)
    counter += 1

## while with a flag
active = True
while active:
    print("Hello")
    active = False

## while with updating an iterable
L = [1, 2, 3]
while L:
    print(L.pop())

## infinite loops
# infinite loops happen when the loop condition never becomes False or if there
# is no break statement inside the loop to exit it

# while True:
#     print("This will run forever unless interrupted")


# nested loops
# ____________

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in matrix:
    for element in row:
        print(element)


# loop control statements
# -----------------------

## break statement
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print(i)


## continue statement
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)  # prints only odd numbers


## pass statement
for _ in range(5):
    pass  # placeholder for future code


# comprehensions
# --------------

## list comprehension
squares = [x**2 for x in range(10)]

## list comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

## list comprehension with if-else
parity = ["even" if x % 2 == 0 else "odd" for x in range(10)]

## dictionary comprehension
square_dict = {x: x**2 for x in range(10)}

## set comprehension
square_set = {x**2 for x in range(10)}

## generator expression
square_gen = (x**2 for x in range(10))


# one-liner loops (bad practice, avoid using)
# -------------------------------------------

for item in L: print(item)  # fmt: skip  # noqa

count = 0
while count <= 3: print(count); count += 1  # fmt: skip  # noqa


# for-else and while-else
# ------------------------------

numbers = [2, 4, 6, 8, 10]

## searching for an odd number using a for loop with a flag
found = False
for num in numbers:
    if num % 2 != 0:
        print("Found an odd number!")
        found = True
        break

if not found:
    print("No odd numbers found")

## searching for an odd number using a for-else clause (no flag needed)
for num in numbers:
    if num % 2 != 0:
        print("Found an odd number!")
        break
else:  # executed if the loop completes without a break
    print("No odd numbers found")

## while-else clause
count = 0
max_count = 5
while count < max_count:
    if count == 10:
        print("Count reached 10!")
        break
    count += 1
else:  # executed if the loop completes without a break
    print("Count did not reach 10")
