import asyncio
import time


def sync_worker(task_id: int) -> int:
    print(f"Worker {task_id} starting...")
    time.sleep(1)  # simulate work
    print(f"Worker {task_id} finished")
    return task_id


async def async_worker(task_id: int) -> int:
    print(f"Worker {task_id} starting...")
    await asyncio.sleep(1)  # yield control to the event loop
    print(f"Worker {task_id} finished")
    return task_id


def run_sync_workers(num_workers: int = 10) -> list[int]:
    data = []

    start = time.perf_counter()
    for i in range(num_workers):
        result = sync_worker(i)
        data.append(result)
    end = time.perf_counter()

    print(f"Total time: {end - start:.2f} seconds (synchronous)")

    return data


async def run_async_workers(num_workers: int = 10) -> list[int]:
    data = []

    start = time.perf_counter()
    tasks = [asyncio.create_task(async_worker(i)) for i in range(num_workers)]
    results = await asyncio.gather(*tasks)
    data.extend(results)
    end = time.perf_counter()

    print(f"Total time: {end - start:.2f} seconds (asynchronous)")

    return data


if __name__ == "__main__":
    # sync code
    run_sync_workers()

    # async code
    asyncio.run(run_async_workers())
