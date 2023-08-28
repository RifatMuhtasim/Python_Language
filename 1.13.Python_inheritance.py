'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''

# Parent Class
class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	def print_name(self):
		print(f"My name is {self.first_name} {self.last_name}")
z = Person("Rifat", "Mustang")
z.print_name()


# Child Class
class Student(Person):
	def __init__(self, first_name, last_name):
		Person.__init__(self, first_name, last_name)

x = Student("Shariful", "Islam")
x.print_name()


# Child class with Super() function: Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
	def __init__(self, first_name, last_name, year):
		super().__init__(first_name, last_name)
		self.graduation_year = year
	def welcome(self):
		print(f"Welcome {self.first_name} {self.last_name} to the class of {self.graduation_year}")

y = Student("Abdullah Al", "Masum", 2024 )
y.welcome()