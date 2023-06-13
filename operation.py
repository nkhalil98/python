import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number1", help="first number")
parser.add_argument("number2", help="second number")
parser.add_argument(
    "operation", help="operation", choices=["add", "subtract", "multiply"]
)

# Adding '--' makes agruments optional but now we have to specify their name when running the file

args = parser.parse_args()

n1 = int(args.number1)
n2 = int(args.number2)
result = None

if args.operation == "add":
    result = n1 + n2
elif args.operation == "subtract":
    result = n1 - n2
elif args.operation == "multiply":
    result = n1 * n2

print("Result:", result)
