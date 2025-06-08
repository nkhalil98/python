import time
import sys


def main():
    global num, increase
    print("*" * num**2)
    if increase:
        num += 1
        if num == 9:
            increase = False
    else:
        num -= 1
        if num == 1:
            increase = True


if __name__ == "__main__":
    num = 1
    increase = True
    try:
        while True:
            main()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
