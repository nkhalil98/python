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
