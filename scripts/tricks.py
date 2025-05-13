# methods that mutate the list in place return None
L1 = [2, 1]
L2 = [3]
L3 = L2.append(L1)  # L3 = None
L4 = L1.sort()  # L4 = None
L5 = sorted(L1)  # L5 = [1, 2]


# iterating over a list while mutating it

## iteration sequence pre-determined at the start of the loop
L = [1, 2, 3, 4]

for i in range(len(L)):
    L.append(i)

## L is mutated each iteration
L = [1, 2, 3, 4]
i = 0

for e in L:  # infinite loop
    L.append(i)
    i += 1

## L is mutated each iteration but not in-place
L = [1, 2, 3, 4]
for e in L:  # iterate over the original list
    L = L + L
print(L)  # [1, 2, 3, 4, 1, 2, 3, 4, ...]

## L is mutated each iteration
L = [1, 2, 2, 2]
for e in L:  # iterate over the original list
    L.remove(2)
print(L)  # [1, 2]


# use id to check objects in memory
