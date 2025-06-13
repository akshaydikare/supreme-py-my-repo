# Python Data Types Example
# This script demonstrates various built-in data types in Python.   
# Text Type: str
text_string = "Hello, Python!"
print(f"Type of '{text_string}': {type(text_string)}")
print(f"Value: {text_string}")

# Numeric Types: int, float, complex
integer_number = 42
print(f"\nType of {integer_number}: {type(integer_number)}")
print(f"Value: {integer_number}")

float_number = 3.14159
print(f"Type of {float_number}: {type(float_number)}")
print(f"Value: {float_number}")

complex_number = 1 + 2j
print(f"Type of {complex_number}: {type(complex_number)}")
print(f"Value: {complex_number}")

# Sequence Types: list, tuple, range
my_list = [1, 2, 'apple', 3.14]
print(f"\nType of {my_list}: {type(my_list)}")
print(f"Value: {my_list}")

my_tuple = (10, 20, 'banana')
print(f"Type of {my_tuple}: {type(my_tuple)}")
print(f"Value: {my_tuple}")

my_range = range(5)
print(f"Type of {my_range}: {type(my_range)}")
print(f"Value: {list(my_range)}") # Convert range to list for printing

# Mapping Type: dict
my_dict = {"name": "Alice", "age": 30}
print(f"\nType of {my_dict}: {type(my_dict)}")
print(f"Value: {my_dict}")

# Set Types: set, frozenset
my_set = {1, 2, 3, 2}
print(f"\nType of {my_set}: {type(my_set)}")
print(f"Value: {my_set}") # Duplicate 2 is removed

my_frozenset = frozenset({1, 2, 3})
print(f"Type of {my_frozenset}: {type(my_frozenset)}")
print(f"Value: {my_frozenset}")

# Boolean Type: bool
boolean_true = True
print(f"\nType of {boolean_true}: {type(boolean_true)}")
print(f"Value: {boolean_true}")

boolean_false = False
print(f"Type of {boolean_false}: {type(boolean_false)}")
print(f"Value: {boolean_false}")

# Binary Types: bytes, bytearray, memoryview (Less common for basic examples)
bytes_data = b"hello"
print(f"\nType of {bytes_data}: {type(bytes_data)}")
print(f"Value: {bytes_data}")

bytearray_data = bytearray(b"world")
print(f"Type of {bytearray_data}: {type(bytearray_data)}")
print(f"Value: {bytearray_data}")

# None Type: NoneType
none_variable = None
print(f"\nType of {none_variable}: {type(none_variable)}")
print(f"Value: {none_variable}")