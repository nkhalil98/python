import multiprocessing
import time

n = 10_000


def square(num: int) -> int:
    sum = 0
    for i in range(num):
        sum += i * i
    return sum


if __name__ == "__main__":
    # without multiprocessing
    start = time.time()
    result = []
    for i in range(n):
        result.append(square(i))
    end = time.time()
    print(f"Time taken without multiprocessing: {end - start}")

    # with multiprocessing
    start = time.time()
    pool = multiprocessing.Pool()
    result = pool.map(square, range(n))
    pool.close()
    pool.join()
    end = time.time()
    print(f"Time taken with multiprocessing: {end - start}")

    # NOTE: it is possible that the time taken with multiprocessing is more than the time taken without multiprocessing
    # due to the overhead of creating and managing processes. The performance improvement with multiprocessing is
    # more evident when the function being executed is computationally expensive.
