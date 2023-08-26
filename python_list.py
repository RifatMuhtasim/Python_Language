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