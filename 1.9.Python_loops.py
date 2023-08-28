# While Loops
i = 1
while i < 6:
	print(i)
	i += 1

# While loops with break and continue
i = 0
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1


i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)



# Python for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break

for x in range(10):
	print(x)
	if x == 5:
		break

# Else in For Loop
for x in range(6):
	print(x)
else:
	print("Finally Finished")