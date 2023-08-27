"""
Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# Getting the Data Type
x = 5
print(type(x)) # Output: <class'int'>
y = 1j
print(type(y))
z = ("apple", "banana", "cherry")
print(type(z))
print(z[2])
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = None
print(type(x))
x = memoryview(bytes(10))
print(x) # Output: <memory at 0x7f26acf362c0>
print(type(x))


# Python Numbers: int, float, complex
x = 1
y = 3.56
z = 35e3
print("Python numbers type:", type(x), type(y), type(z))

# convert from float to  int
convert_y = int(y)
print(convert_y, type(convert_y)) # Output: 3 <class 'int'>

# Random number generate
import random
print(random.randrange(1, 10))


# Python String 
a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("length:", len(a))

# Strings are Arrays
a = "Hello World"
print(a[6])

# Looping Through a String
for x in "Hello World":
	print(x)

# Check String
text = "The quick brown fox jumps over lazy dog. "
print("fox" in text) # Output: True
print("dog" not in text)

# Slicing
print(text[4:])
print(text[1:10])

# Python Modify String
print(text.upper())
print(text.lower())
print(text.strip()) # remove this unusal space.

# Replace String
print(text.replace("dog", "cow"))
# Split String
print(text.split(" "))

# String Format
age = 22
print(f"My age is {age}")


# Python Booleans
print(10 == 9)
x = 200
print(isinstance(x, int))