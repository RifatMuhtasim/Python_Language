# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression

x = lambda a : a + 365
print(x(50))

y = lambda x, y : x + y 
print(y(10, 30))

# use lambda as an anonymous function inside another function
def my_function(n):
	return lambda a: a * n
my_doubler = my_function(2)
print(my_doubler(11))


def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))



# Array
cars = ["Ford", "Volvo", "BMW"]
print(cars)
cars.append("Ferrari")
print(cars)