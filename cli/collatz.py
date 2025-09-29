import time
import sys


def collatz(n: int) -> int:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    return n


if __name__ == "__main__":
    n = input("Enter a positive integer: ")

    try:
        n = int(n)
    except ValueError:
        print("Please enter a positive integer")
        sys.exit(1)

    if n <= 0:
        print("Please enter a positive integer")
        sys.exit(1)

    try:
        while n != 1:
            n = collatz(n)
            print(n, end=" ", flush=True)
            time.sleep(0.1)
        print("\nReached 1, exiting")
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
