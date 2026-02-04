import sys


def main():
    print("Executing cumsum1.py")

    args = sys.argv[1:]
    csum = 0

    for arg in args:
        try:
            num = int(arg)
            csum += num
            print(f"Adding {num}, current cumulative sum: {csum}")
        except ValueError:
            print(f"Invalid integer: {arg}")
            sys.exit(1)

    print("cumsum1.py executed successfully")


if __name__ == "__main__":
    main()
