'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("Something else went wrong")


#2
try:
  	print("Hello")
except:
  	print("Something went wrong")
else:
  	print("Nothing went wrong")

# 3
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# Raise an exception
x = -1

if x < 0:
	raise Exception("Sorry, No numbers below Zero")