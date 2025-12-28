import datetime as dt
import re
import string


from collections import UserString


# TODO: nested f-strings
# TODO: t-strings (new)
# TODO: regex (search - sub - findall - match - fullmatch - compile)
# TODO: parsing datatime strings


# string creation
# ---------------

## string literals
my_string1 = "Hello, World!"  # double quotes
my_string2 = 'Hello, World!'  # fmt:skip  # single quotes
empty = ""  # initialize an empty string
empty2 = str()  # initialize an empty string

## mixing single and double quotes
quote = "He's a great guy"
quote2 = 'She said "Hello"'

## multiline strings
multiline_str = """This is a
multiline string.
It can span multiple lines."""

multiline_str2 = '''This is another
multiline string.
It can also span multiple lines.'''  # fmt:skip

# strings cannot be created with backticks


# escape characters
# -----------------

print("Hello, \nWorld!")  # newline
print("Hello, \tWorld!")  # tab
print("Hello, \bWorld!")  # backspace
print("Hello, \rWorld!")  # carriage return
print("Hello, \fWorld!")  # form feed
print("Hello, \vWorld!")  # vertical tab
print("Hello, \aWorld!")  # bell


# strings are sequences
# ----------------------

fruit = "banana"

## length
length = len(fruit)

## indexing and slicing
first_char = fruit[0]  # indexing
last_char = fruit[-1]  # negative indexing
substring = fruit[2:4]  # slicing

## concatenation
dessert = fruit + " split"

## repetition
doubled = fruit * 2

## membership testing
has_a = "a" in fruit  # True
has_z = "z" in fruit  # False

## strings are immutable
# fruit[0] = "B"  # TypeError
fruit = "B" + fruit[1:]  # creates a new string


# string formatting
# -----------------

## various ways to format strings
first = "ada"
last = "lovelace"
full_name_1 = first + " " + last
full_name_2 = f"{first} {last}"  # f-string (introduced in Python 3.6)
full_name_3 = "{} {}".format(first, last)  # format method
full_name_4 = "{1} {0}".format(last, first)  # format method with positional args
full_name_5 = "{first} {last}".format(
    first=first, last=last
)  # format method with keyword args
full_name_6 = "%s %s" % (first, last)  # old-style/C formatting

## format specifiers
pi = 3.14159
formatted_pi = f"{pi:.2f}"  # f-string with 2 decimal places

number = 42
formatted_number = f"{number:x}"  # f-string with hexadecimal format

decimal_number = 255
binary_format = f"{decimal_number:b}"  # binary format


# string methods
# --------------

## case manipulation
name = "ada lovelace"
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.swapcase())

## stripping whitespace
name = " ada lovelace "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

## removing prefixes and suffixes
url = "https://www.example.com"
url = url.removeprefix("https://www.")
url = url.removesuffix(".com")
print(url)

## padding
num = 42
print(str(num).rjust(5))  # right justify
print(str(num).ljust(5))  # left justify
print(str(num).center(5))  # center
print(str(num).zfill(5))  # zero fill

## splitting and joining
words = "hello,world,python"
words = words.split(",")  # split a string into a list

words = ["hello", "world", "python"]
words = "-".join(words)  # join a list into a string

## finding substrings
fruit = "banana"
print(fruit.find("a"))  # 1
print(fruit.find("z"))  # -1
print(fruit.index("a"))  # 1
# print(fruit.index("z"))  # ValueError
print(fruit.count("a"))  # 3
print(fruit.startswith("b"))  # True
print(fruit.endswith("a"))  # True

## replacing substrings
fruit = "banana"
fruit = fruit.replace("a", "o")
print(fruit)


# string comparison
# -----------------

# lexicographical comparison (based on Unicode code points)
"a" > "b"  # False
"a" < "b"  # True
"ab" > "aa"  # True
"abc" < "abcd"  # True


# raw strings and bytes
# ---------------------

raw_str = r"C:\Users\Name\Documents"  # raw string (backslashes are treated literally so no need to escape)
byte_data = b"Hello, World!"  # bytes literal


# ASCII: ord() and chr()
# ---------------------
char = "A"
ascii_value = ord(char)  # 65
print(ascii_value)

ascii_char = chr(65)  # "A"
print(ascii_char)

# !r __repr__ vs !s __str__ vs !a __ascii__
# -----------------------------------------


# printing and formatting strings calls the __str__() method. If __str__() is
# not defined, __repr__() is called. we can call the __repr__() method directly
# using !r like so:


class Example:
    def __str__(self):
        return "str-version"

    def __repr__(self):
        return "repr-version"


obj = Example()

print(f"Default: {obj}")  # uses __str__ if available
print(f"!s: {obj!s}")  # forces str() -> __str__
print(f"!r: {obj!r}")  # forces repr() -> __repr__
print(f"!a: {'Hello\nWorld'!a}")  # forces ascii(), escapes non-ASCII/whitespace
