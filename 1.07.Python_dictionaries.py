# Dictionaries are used to store data values in key:value pairs.

thisdict = {
 	'brand': "Ford",
  	"model": "Mustang",
  	"year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))

# The dict() Constructor
dict2 = dict(name="Rifat Muhtasim", age=22, country="Bangladesh")
print(dict2)
dict2_keys = dict2.keys() # Show the keys value
print(dict2_keys)
dict2_values = dict2.values() # Show the dict2 values
print(dict2_values)
print(dict2.items()) # Show the items value 

# Check if Key Exists
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change Dictionary Items
thisdict["model"] = "Ferrari"
print(thisdict)
thisdict.update({"year": 2000})
print(thisdict)


# Add Dictionary Items
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"owner": "Rifat"})
print(thisdict)


# Remove Dictionary Items
thisdict.pop("color")
print(thisdict)
thisdict.popitem() # Delete the last item
print(thisdict)


# Loop Dictionaries
for x in thisdict: # Show all the key
	print(x)

for x in thisdict:
	print(thisdict[x]) # Show all the values

for x in thisdict.values():
	print(x)

for x,y in thisdict.items():
	print(y,x)


# Copy Dictionaries
my_dict = dict(thisdict)
print(my_dict)
my_dict2 = thisdict.copy()
print(my_dict2)


# Methods of dictionary
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''