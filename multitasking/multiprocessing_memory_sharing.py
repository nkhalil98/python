import multiprocessing
from multiprocessing.sharedctypes import SynchronizedArray, Synchronized


def populate_data(
    data: list[int],
    result: SynchronizedArray,
    val: Synchronized,
) -> list[int]:
    for index, item in enumerate(data):
        val.value += 1
        result[index] = item * item
    return result


if __name__ == "__main__":
    data = [1, 2, 3]
    result = multiprocessing.Array("i", len(data))
    val = multiprocessing.Value("i", 0)
    p = multiprocessing.Process(target=populate_data, args=(data, result, val))
    p.start()
    p.join()
    print(result[:])  # Output: [1, 4, 9]
    print(val.value)  # Output: 3
