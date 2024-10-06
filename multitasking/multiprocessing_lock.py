import multiprocessing
from multiprocessing.sharedctypes import Synchronized
from multiprocessing.synchronize import Lock


def add_one(num: Synchronized):
    for _ in range(1000):
        num.value += 1


def subtract_one(num: Synchronized):
    for _ in range(1000):
        num.value -= 1


def add_one_with_lock(num: Synchronized, lock: Lock):
    for _ in range(1000):
        lock.acquire()
        num.value += 1
        lock.release()


def subtract_one_with_lock(num: Synchronized, lock: Lock):
    for _ in range(1000):
        with lock:  # same as lock.acquire() and lock.release()
            num.value -= 1


if __name__ == "__main__":
    x = multiprocessing.Value("i", 0)
    p1 = multiprocessing.Process(target=add_one, args=(x,))
    p2 = multiprocessing.Process(target=subtract_one, args=(x,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("without lock:", x.value)  # Output is not guaranteed to be 0

    y = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()
    p3 = multiprocessing.Process(target=add_one_with_lock, args=(y, lock))
    p4 = multiprocessing.Process(target=subtract_one_with_lock, args=(y, lock))

    p3.start()
    p4.start()

    p3.join()
    p4.join()

    print("with lock:", y.value)  # Output is guaranteed to be 0
