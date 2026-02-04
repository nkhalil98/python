import csv
import logging
import json
import pickle
import shelve
import socket
import sqlite3
from pathlib import Path
from pprint import pprint


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# TODO: pickle and shelve
# TODO: sqlite3
# TODO: network io


# printing/output
# ---------------

## printing (to stdout by default)
print("Hello, World!")


## print can take any number of arguments and will convert them to strings
print("Hello", "World", 42)


## print adds a space between arguments and a newline at the end by default
print("first", "line")
print("second", "line")


## print with more options
with open("hello.txt", "w") as f:
    print("Hello", "World", 67, sep=", ", end=".\n", file=f)


## flush
print(
    "Hello, World!", flush=True
)  # flush the stream after printing (useful for real-time output)

# print() calls the __str__() method of each object passed to it


## pretty-printing
people = [
    {
        "name": "Nabil",
        "id": 1,
        "age": 26,
    },
    {
        "name": "Alice",
        "age": 25,
        "id": 2,
    },
    {
        "name": "Bob",
        "age": 24,
        "id": 3,
    },
]

print(people)
pprint(people, indent=2)  # pretty-printing with indentation

# for more advanced output, use the logging module


# user input
# ----------

## user input (reads from stdin)
prompt = "What is your name? "
user_input = input(prompt)
print(user_input)


## input() always returns a string
age = int(input("Enter your age: "))  # type casting to int


## 'advanced' user input
a, b, c = map(int, input().split())  # reading multiple integers from a single line
print("a:", a, "b:", b, "c:", c)


# file io
# -------

# there are two types of files: text and binary
# text files are human-readable
# binary files are machine-readable


## reading the entire file
f = open("filename.txt")
content = f.read()
lines = content.splitlines()
for line in lines:
    print(line)
f.close()  # close the file to free up resources


## reading line by line
f = open("filename.txt")
for line in f:
    print(line.rstrip())  # remove trailing whitespace
f.close()


## reading all lines
f = open("filename.txt")
lines = f.readlines()
for line in lines:
    print(line)
f.close()


## using with statement (context manager)
with open("filename.txt") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        print(line)

print(f.closed)  # file is automatically closed after with block


## pathlib

### reading an entire file
path = Path("filename.txt")
contents = path.read_text().rstrip()
print(contents)


### reading a file line by line
path = Path("filename.txt")
lines = path.read_text().splitlines()
for line in lines:
    print(line)


### writing to a file
path = Path("filename3.txt")
path.write_text("I love Python\n")


# serialization/deserialization
# -----------------------------

## json
data = {"name": "Nabil", "age": 26}

### writing to a file
p = Path("data.json")
data_str = json.dumps(data)  # Serialize Python object (dict) to JSON string
p.write_text(data_str)


### reading from a file
data_str = p.read_text()
data = json.loads(data_str)  # Deserialize JSON string into Python object (dict)


### can also read/write directly to/from files
with open("data.json") as f:
    data = json.load(f)


### another json example
def add_data_point(json_string, name, age):
    data = json.loads(json_string)
    data[name] = age
    return json.dumps(data)


json_str = '{"Alice": 25, "Bob": 24}'
new_json_str = add_data_point(json_str, "Nabil", 26)
print(new_json_str)


## csv

### without csv module
with open("stonks.csv", "r") as f, open("pe1.csv", "w") as out:
    out.write("Company Name,PE Ratio\n")  # write header pe1.csv
    next(f)  # skip header line in stonks.csv
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        pe = round(price / eps, 2)
        out.write(f"{stock},{pe}\n")

### with csv module
with open("stonks.csv", "r") as f, open("pe2.csv", "w", newline="") as out:
    reader = csv.reader(f)
    writer = csv.writer(out)
    writer.writerow(["Company Name", "PE Ratio"])
    next(reader)
    for row in reader:
        stock = row[0]
        price = float(row[1])
        eps = float(row[2])
        pe = round(price / eps, 2)
        writer.writerow([stock, pe])
