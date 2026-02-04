import decimal
import fractions
import math
import numbers
import random
import statistics

# TODO: more on float precision and representation issues
# TODO: more on float() parsing from strings


# python as a calculator
# ----------------------

print(2 + 3)  # operand -> operator -> operand -> result (value)
print(2 * 3)
print(2**3)


# int
# ---

# python integers are ubounded (limited by available memory)
n = 1
m = 1_000_000  # underscores for readability
p = 0  # initialize an "empty" integer
q = int()  # another way


# float
# -----

# python floating point numbers are represented using double precision (64 bit)
# as per IEEE 754 standard
x1 = 0.1
x2 = 0.2
sum_ = x1 + x2
print(sum_)  # 0.30000000000000004 (floating point error)
x3 = 1e-3  # scientific notation
x4 = 1.0e3
x5 = float(5)
x0 = 0.0  # initialize an "empty" integer
x00 = float()  # another way


# complex
# -------

z = 1 + 2j
print(f"Real: {z.real}, Imaginary: {z.imag}")


# decimal
# -------

d1 = decimal.Decimal("0.1")  # use strings to avoid float precision issues
d2 = decimal.Decimal("0.2")
print(d1 + d2)  # 0.3


# fractions
# ---------

f1 = fractions.Fraction(1, 3)
f2 = fractions.Fraction(2, 3)
print(f1 + f2)  # 1


# arithmetic operations
# ---------------------

a = 10
b = 3
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division (float)
print(a // b)  # floor division
print(a % b)  # modulus
print(a**b)  # exponentiation
print(a + (b * 2) - (a / b))


# arithmetic functions
# --------------------

## built-in functions
print(abs(-5))  # 5
print(round(3.14159, 2))  # 3.14
print(pow(2, 3))  # 8

### python rounding behavior (IEEE 754 "bankers' rounding")
print(round(2.5))  # 2  (rounded to nearest even number)
print(round(3.5))  # 4


## math module
print(math.sqrt(16))  # 4.0
print(math.sin(math.pi / 2))  # 1.0
print(math.log(100, 10))  # 2.0


## statistics module
data = [1, 2, 3, 4, 5]
print(statistics.mean(data))  # 3
print(statistics.median(data))  # 3
print(statistics.stdev(data))  # 1.5811388300841898

## random module
print(random.random())  # random float between 0.0 and 1.0 from uniform distribution
print(random.randint(1, 10))  # random integer between 1 and 10 (inclusive)
