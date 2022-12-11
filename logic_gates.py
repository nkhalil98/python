def NAND_gate(a, b):
  if a:
    if b:
      return 0
  return 1

# Truth Table
print("NAND Gate Truth Table:\n")
print("A: 0, B: 0 | Output: {0}".format(NAND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(NAND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(NAND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}\n".format(NAND_gate(1, 1)))

def NOT_gate(a):
  return int(not a)

# Truth Table
print("NOT Gate Truth Table:\n")
print("A: 0 | Output: {0}".format(NOT_gate(0)))
print("A: 1 | Output: {0}\n".format(NOT_gate(1)))

def AND_gate(a,b):
  return int(a and b)

# Truth Table
print("AND Gate Truth Table:\n")
print("A: 0, B: 0 | Output: {0}".format(AND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(AND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(AND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}\n".format(AND_gate(1, 1)))

def OR_gate(a,b):
  return int(a or b)

# Truth Table
print("OR Gate Truth Table:\n")
print("A: 0, B: 0 | Output: {0}".format(OR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(OR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(OR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}\n".format(OR_gate(1, 1)))

def XOR_gate(a,b):
  return int(a and not b) or int(not a and b)

# Truth Table
print("XOR Gate Truth Table:\n")
print("A: 0, B: 0 | Output: {0}".format(XOR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(XOR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(XOR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}\n".format(XOR_gate(1, 1)))
