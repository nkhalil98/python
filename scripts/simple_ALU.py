from logic_gates import *

# opcode | function
#   00   | input a and b into a half-adder
#   01   | input a, b, and c into a full adder
#   10   | increment a by 1
#   11   | increment b by 1


def half_adder(a, b):
    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return (s, c)


def full_adder(a, b, c):
    s, c_1 = half_adder(a, b)
    Sum, c_2 = half_adder(s, c)
    c_out = OR_gate(c_1, c_2)
    return (Sum, c_out)


def ALU(a, b, c, opcode):
    if opcode == "00":
        return half_adder(a, b)
    elif opcode == "01":
        return full_adder(a, b, c)
    elif opcode == "10":
        return XOR_gate(a, 1)
    elif opcode == "11":
        return XOR_gate(b, 1)
    else:
        print("Invalid opcode")
