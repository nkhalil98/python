import multiprocessing
import time

from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Literal

WorkerType = Literal["io", "cpu"]
MAX_WORKERS = 5
DATA_SIZE = 100_000_000


def io_worker(task_id: int, duration: int = 1) -> int:
    print(f"Worker {task_id} starting...")
    time.sleep(duration)  # simulate I/O-bound work
    print(f"Worker {task_id} finished")
    return task_id


def computing_worker(task_id: int, data_size: int = DATA_SIZE) -> int:
    print(f"Worker {task_id} starting...")
    for _ in range(data_size):
        pass  # simulate CPU-bound work
    print(f"Worker {task_id} finished")
    return task_id


def run_sync_workers(worker_type: WorkerType, num_workers: int = 10) -> list[int]:
    data = []
    worker = io_worker if worker_type == "io" else computing_worker

    start = time.perf_counter()
    for i in range(num_workers):
        result = worker(i)
        data.append(result)
    end = time.perf_counter()

    print(f"Total time: {end - start:.2f} seconds (synchronous)")

    return data


def run_parallel_workers(worker_type: WorkerType, num_workers: int = 10) -> list[int]:
    data = multiprocessing.Manager().list()
    worker = io_worker if worker_type == "io" else computing_worker

    start = time.perf_counter()
    processes = []
    for i in range(num_workers):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    end = time.perf_counter()

    print(f"Total time: {end - start:.2f} seconds (multiprocessing)")

    return data


def run_process_pool_executor(
    worker_type: WorkerType, num_workers: int = 10
) -> list[int]:
    data = multiprocessing.Manager().list()
    worker = io_worker if worker_type == "io" else computing_worker

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(worker, i) for i in range(num_workers)]
        for future in as_completed(futures):
            result = future.result()
            data.append(result)
    end = time.perf_counter()

    print(
        f"Total time: {end - start:.2f} seconds (ProcessPoolExecutor) with {MAX_WORKERS} workers"
    )

    return data


if __name__ == "__main__":
    # sync code
    run_sync_workers("cpu")

    # multiprocessing code
    run_parallel_workers("cpu")

    # ProcessPoolExecutor code
    run_process_pool_executor("cpu")
