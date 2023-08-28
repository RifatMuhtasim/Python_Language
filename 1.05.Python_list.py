'''
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

fruit_list = ["apple", "banana", "cherry"]
print(fruit_list)
print(len(fruit_list)) # length of the list

list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(list1[-1])
print(list1[2:])

# Check if Item Exists
if "male" in list1:
	print(True)

# Change Item Value
fruit_list[1] = "mango"
print(fruit_list)
fruit_list[1:2] = ["blackcurrant", "watermelon"]
print(fruit_list)

# Append Items
fruit_list.append("orange")
print(fruit_list)

# Insert Items
fruit_list.insert(0, "pineapple")
print(fruit_list)


web_development_skills = ["Python", "Django", "Javascript", "React", "HTML", "CSS", "Bootstrap"]
business_skills = ["Blockchain Developer", "Full-stack Web Developer", "SEO Specialist", "DNS Specialist"]

# Extend List
business_skills.extend(web_development_skills)
print(business_skills)
print(web_development_skills + business_skills)

# Remove Specified Item
web_development_skills.remove("CSS")
print(web_development_skills)

# Remove Specified Index
web_development_skills.pop() # Remove the last item
print(web_development_skills)
business_skills.pop(0)
print(business_skills)

del web_development_skills[0] # Remove the fist item
print(web_development_skills)

# Clear the List
business_skills.clear()
print(business_skills)


# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
for i in range(len(thislist)):
	print(i)


# Using a While Loop
print("Using While Loop")
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# newlist2 = [expression for item in iterable if condition == True]
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)
list1 = [x for x in range(5)]
print(list1)

upper_list = [x.upper() for x in fruits]
print(upper_list)


# Sort Descending
upper_list.sort(reverse=True)
print(upper_list)


# Customize Sort Function
def my_fun(n):
  return abs(n-60)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = my_fun)
print(thislist)


# Reverse Order
thislist.reverse()
print(thislist)


# Copy a List
new_fruit_list = fruits.copy()
print(new_fruit_list)


# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 # 1 
list3.extend(list2) # 2
print(list3)

for x in list2:
  list1.append(x) # 3
print(list1)




# List Methods
'''
append()  Adds an element at the end of the list
clear() Removes all the elements from the list
copy()  Returns a copy of the list
count() Returns the number of elements with the specified value
extend()  Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert()  Adds an element at the specified position
pop() Removes the element at the specified position
remove()  Removes the item with the specified value
reverse() Reverses the order of the list
sort()  Sorts the list
'''













