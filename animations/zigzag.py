import time
import sys


def main():
    global indent, increase
    print(" " * indent + "*" * 10)
    if increase:
        indent += 1
        if indent == 20:
            increase = False
    else:
        indent -= 1
        if indent == 0:
            increase = True


if __name__ == "__main__":
    indent = 0
    increase = True
    try:
        while True:
            main()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
