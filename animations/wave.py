import time
import sys


def main():
    global num, increase
    colors = [
        "\033[31m",  # red
        "\033[32m",  # green
        "\033[33m",  # yellow
        "\033[34m",  # blue
        "\033[35m",  # purple
        "\033[36m",  # cyan
        "\033[37m",  # white
    ]
    color = colors[num % len(colors)]
    print(f"{color}*" * num**2 + "\033[0m")
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
