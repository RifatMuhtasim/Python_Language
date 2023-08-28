'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

a = 100
b = 100
if a > b:
	print("A is Greater than B")
elif a == b:
	print("A and B are equal")
else:
	print("B is greater than A")


# Short Hand If
if a > b : print("A is greater than B")

# Short Hand If ... Else
print("A is greater than B") if a > b else print("B is greater than A")
# Ternary Operators [operation if condition else operation if condition else operation]
print("A is greater than B") if a > b else print("B is greater than A") if b > a else print("both of them are equal")


# AND, OR, NOT
a = 200
b = 333
c = 500
if a > b and c > a:
	print("Both of the condition are must true")
if a > b or c > a:
	print("At least one of the condition is True")
if not a > b:
	print("A is not greater than B")
if c > a:
	pass