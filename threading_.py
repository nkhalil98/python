import threading
import time


n = list(range(20))


def square(l: list[int]) -> list[int]:
    l2 = []
    for i in l:
        time.sleep(0.1)  # artificial time delay
        l2.append(i * i)
    return l2


def cube(l: list[int]) -> list[int]:
    l3 = []
    for i in l:
        time.sleep(0.1)  # artificial time delay
        l3.append(i * i * i)
    return l3


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
