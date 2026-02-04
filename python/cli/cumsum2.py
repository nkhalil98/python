import argparse


def main():
    print("Executing cumsum2.py")

    parser = argparse.ArgumentParser(
        description="Calculate cumulative sum of integers."
    )
    parser.add_argument(
        "numbers",
        type=int,
        nargs="+",
        help="Integers to sum",
    )
    args = parser.parse_args()
    nums = args.numbers

    csum = 0

    for num in nums:
        csum += num
        print(f"Adding {num}, current cumulative sum: {csum}")

    print("cumsum2.py executed successfully")


if __name__ == "__main__":
    main()
