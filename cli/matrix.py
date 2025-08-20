import os
import random
import sys
import time

try:
    terminal_size = os.get_terminal_size()
    WIDTH = terminal_size.columns
except OSError:
    WIDTH = 80


def main():
    columns = [0] * WIDTH
    for i in range(WIDTH):
        if random.random() < 0.1:
            columns[i] = random.randint(10, 15)

        if columns[i] == 0:
            print(" ", end="")
        else:
            num = random.randint(0, 9)
            print(f"\033[32m{num}\033[0m", end="")
            columns[i] -= 1
    print()  # newline at the end of the row


if __name__ == "__main__":
    try:
        while True:
            main()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
