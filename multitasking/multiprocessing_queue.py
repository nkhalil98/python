import multiprocessing
from multiprocessing.queues import Queue


def populate_data(data: list[int], q: Queue) -> list[int]:
    for i in data:
        q.put(i * i)


if __name__ == "__main__":
    data = [1, 2, 3]
    q = multiprocessing.Queue()  # queue that lives in shared memory
    p = multiprocessing.Process(target=populate_data, args=(data, q))
    p.start()
    p.join()
    while not q.empty():
        print(q.get())
