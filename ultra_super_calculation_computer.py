#-------------------------------------------
# USCC Headquarter's Instruction Set Architecture
#  System Design:
#   - Four function calculator
#   - Can only operate on numbers stored in registers
#   - Processor receives binary data as 32-bit strings
#   - Returns results to the terminal
#   - Can operate on 10-bit numbers (0 thru 1023)
#   - Results can be negative (5 - 10 = -5)
#  Instruction format:
#   - 32 bit's in length
#   - Binary data will come to the CPU as a string
#   - Registers (32 total on CPU, 0-indexed)
#      - 0 thru 21:  Available for number storage
#        - 0: Constant 0
#      - 22 thru 31: Available for history storage
# +=======+=======+=======+=======+=======+=======+=======+=======+
# | 0: 0  | 1:    | 2:    | 3:    | 4:    | 5:    | 6:    | 7:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# | 8:    | 9:    |10:    |11:    |12:    |13:    |14:    |15:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |16:    |17:    |18:    |19:    |20:    |21:    |22: H0 |23: H1 |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |24: H2 |25: H3 |26: H4 |27: H5 |28: H6 |29: H7 |30: H8 |31: H9 |
# +=======+=======+=======+=======+=======+=======+=======+=======+
#   - Bits 0-5 are OPCODEs
#     - use variable 'opcode' in program
#   - Bits 6-10 & 11-15 are source register locations
#     - use variables 'source_one' and 'source_two' in program
#   - Bits 16-25 are reserved for adding a new value to the registers
#     - use variable 'store' in program
#   - Bits 26-31 are functions
#     - use variable 'function_code' in program
# +--------+----------+-------------------------------------+
# | OPCODE | FUNCTION | Definition                          |
# | 000000 |  100000  | Add two numbers from registers      |
# | 000000 |  100010  | Subtract two numbers from registers |
# | 000000 |  011000  | Multiply two numbers from registers |
# | 000000 |  011010  | Divide two numbers from registers   |
# | 000001 |  000000  | Store value to next register        |
# | 100001 |  000000  | Return previous calculation         |
# +--------+----------+-------------------------------------+

# Your code below here:
class UltraSuperCalculator():
  def __init__(self, name):
    self.name = name
    self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.numbers_index = 1
    self.history_index = 0
    self.temp_history_index = 0
    self.user_display = ''
    self.update_display(f"Welcome to {self.name} calculator")

  def update_display(self, to_update):
    self.user_display = to_update
    print(to_update)

  def store_value_to_register(self, value_to_store):
    assert self.numbers_index != 0
    if self.numbers_index > 21:
      self.numbers_index = 1
    else:
      val = int(value_to_store, 2)
      self.number_registers[self.numbers_index] = val
      print(f"Value: {val} stored in Register {self.numbers_index}.")
      self.numbers_index += 1

  def load_value_from_register(self, register_address):
    index = int(register_address, 2)
    val = int(self.number_registers[index])
    return val

  def store_to_history_register(self, result_to_store):
    if self.history_index > 9:
      self.history_index = 0
    else:
      val = bin(result_to_store)
      self.history_registers[self.history_index] = val
      self.history_index += 1
      self.temp_history_index = self.history_index

  def add(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    return num1 + num2
    
  def subtract(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    return num1 - num2

  def multiply(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    return num1 * num2

  def divide(self, address_num1, address_num2):
    num1 = self.load_value_from_register(address_num1)
    num2 = self.load_value_from_register(address_num2)
    if num2 != 0:
      return int(num1 / num2)
    else:
      print("Division by 0 error")
  
  def get_last_calculation(self):
    self.temp_history_index -= 1
    last_value = f"Last calculated value was {int(self.history_registers[self.temp_history_index],2)}"
    self.update_display(last_value)
  
  def binary_reader(self, instruction):
    if len(instruction) != 32:
      print("Invalid instruction length")
      return

    opcode = instruction[0:6]
    source_one = instruction[6:11]
    source_two = instruction[11:16]
    store = instruction[16:26]
    function_code = instruction[26:]

    if opcode == "000001":
      self.store_value_to_register(store)
      return
    elif opcode == "100001":
      self.get_last_calculation()
      return
    elif opcode != "000000":
      self.update_display("Invalid opcode")
      return
    
    result = 0

    if (function_code == '100000'):
      result = self.add(source_one, source_two)
    elif (function_code == '100010'):
      result = self.subtract(source_one, source_two)
    elif (function_code == '011000'):
      result = self.multiply(source_one, source_two)
    elif (function_code == '011010'):
      result = self.divide(source_one, source_two)
    else:
      self.update_display("Invalid Function")
      return

    self.store_to_history_register(result)
    self.update_display(f"The result is: {result}")
    return