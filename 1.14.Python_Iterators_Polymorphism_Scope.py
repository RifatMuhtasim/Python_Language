'''
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''

print("Hello World")

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Python Polymorphisom
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))


# Global Keyword
def my_fuction():
    global x
    x = 10
my_fuction()
print(x)


# Modules
import mymodule
mymodule.greeting("Rifat Muhtasim")