'''
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
'''

class My_class:
	x = 500
	y = 20 
p = My_class()
print(p.y)

# The __init__() Function: 
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = Person("Rifat Muhtasim", 23)
print(p1.age)


# The __str__() Function: The __str__() function controls what should be returned when the class object is represented as a string.

class Personx:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return f"{self.name} and age is: {self.age}"
p2 = Personx("Shariful Islam", 24)
print(p2)


# Object Methods: Objects can also contain methods. Methods in objects are functions that belong to the object.
class Persony:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def My_function(self):
		print(f"My name is: {self.name} and my age is: {self.age}")
p3 = Persony("Abdullah Al Masum", 54)
p3.My_function()


# Modify Object Properties
p3.age = 22
p3.My_function()

# Delete Object Properties
del p3.age
