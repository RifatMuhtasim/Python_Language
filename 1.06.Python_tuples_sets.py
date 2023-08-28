'''
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
'''

mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple)) # Length of the tuples

tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1)) # Type of the tuple
print(tuple1[0]) # Access of the tuple 
print(tuple1[1:4]) # Range of index

# Loop Through the Index Numbers
for i in range(len(mytuple)):
	print(mytuple[i])


# Python Sets - Start
myset = {"apple", "banana", "cherry"}
for x in myset:
	print(x)

# Add Items
myset.add("orange")
print(myset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Remove Item
thisset.remove("papaya")
print(thisset)

# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


#  Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates
x.symmetric_difference_update(y)
print(x)

# Sets Method 
'''
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''