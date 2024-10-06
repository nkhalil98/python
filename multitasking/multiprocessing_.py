import multiprocessing
import time


def square(l: list[int]) -> list[int]:
    return [x * x for x in l]


def cube(l: list[int]) -> list[int]:
    return [x * x * x for x in l]


if __name__ == "__main__":
    n = list(range(10000000))
    # without multiprocessing
    start = time.time()
    square(n)
    cube(n)
    end = time.time()
    print(f"Time taken without multiprocessing: {end - start}")

    # with multiprocessing
    # create processes
    p1 = multiprocessing.Process(target=square, args=(n,))
    p2 = multiprocessing.Process(target=cube, args=(n,))

    start = time.time()
    # start the processes
    p1.start()
    p2.start()

    # wait for the processes to finish
    p1.join()
    p2.join()

    end = time.time()
    print(f"Time taken with multiprocessing: {end - start}")
