# Python Variables - Case Sensitive 
x = 5 
y = "Data Science"
x = 6
print(x)
 

# Casting
x = float(x)
print(x)
print(type(x)) # Get the type

My_name_variable = "Rifat Muhtasim" # Snake case variable


# Many values to multiple Variables
a, b, c = "Apple", "Banana", "Cherry"
print(b)

# One Value to Multiple Variables
d = e = f = "Mango"
print(d)

fruits = ["Apple", "Banana", "Cherry"]
print(fruits[2])


# Output variable
x = "Data"
y = "Science"
z = "is Awesome"
print(x,y,z)
print(x+" "+y+" "+z)

x = 5
y = 10
print(x+y)


# Global Variable
a = "Data Science"
def my_function():
	global a 
	a = "Python"
	print(a + " is Awesome")	
my_function()
print(a + " is Awesome") # Result: Python is awesome 



