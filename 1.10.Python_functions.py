def my_function():
  print("Hello from a function")

my_function()


# Arbitrary Arguments, *args
def my_function(*kids):
  print("The Youngest child is: " + kids[-1])

my_function("Sakib", "Masum", "Shariful")


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kids):
  print("His Last Name is: " + kids["last_name"])
my_function(first_name="Shariful", last_name="Islam")


# Default Parameter Value
def My_country(country="Bangladesh"):
  print("My country name is : " + country)
My_country("India")
My_country("Singapore")
My_country()


# Passing a List as an Argument
def Fruits(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
Fruits(fruits)

# Return Values
def Return_function(value):
  return value + 365
print(Return_function(699))


# Recursion Function
def Tri_recursion(x):
  if (x > 0):
    result = x + Tri_recursion(x - 1)
    print(result)
  else:
    result = 0
  return result
# The output of the function will be a sequence of numbers, each representing the cumulative sum of the integers from 10 down to 1.
Tri_recursion(10)