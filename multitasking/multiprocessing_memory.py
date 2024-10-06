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
    print(data)
    # Output: []
    # Explanation: Every process has its own memory space. The data list is not
    # shared between the main process and the child process. The child process has
    # its own copy of the data list, which is why the changes made in the child
    # process are not reflected in the main process.

    # To share data between processes, we can use Inter-process Communication (IPC)
    # mechanisms like shared, queues, pipes, etc.
    