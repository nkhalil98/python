import threading
import time


n = list(range(20))


def square(arr: list[int]) -> list[int]:
    arr2 = []
    for i in arr:
        time.sleep(0.1)  # artificial time delay
        arr2.append(i * i)
    return arr2


def cube(arr: list[int]) -> list[int]:
    arr3 = []
    for i in arr:
        time.sleep(0.1)  # artificial time delay
        arr3.append(i * i * i)
    return arr3


# without threading
start = time.time()
square(n)
cube(n)
end = time.time()
print(f"Time taken without threading: {end - start}")

# with threading

# create threads
t1 = threading.Thread(target=square, args=(n,))
t2 = threading.Thread(target=cube, args=(n,))

start = time.time()
# start the threads
t1.start()
t2.start()

# wait for the threads to finish
t1.join()
t2.join()

end = time.time()
print(f"Time taken with threading: {end - start}")
