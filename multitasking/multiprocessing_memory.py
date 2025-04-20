import multiprocessing


data = []


def populate_data(n: int) -> list[int]:
    global data
    for i in range(n):
        data.append(i)
    return data


if __name__ == "__main__":
    p = multiprocessing.Process(target=populate_data, args=(10000000,))
    p.start()
    p.join()
    print(data)  # Output: []
