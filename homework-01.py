"""
Name: Omar Trejo
Email: otrejo0221@my.mwsu.edu
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

# A:--------------------------------------------------------
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Print: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

# B:--------------------------------------------------------
x = [3, 1, 2, 1, 5, 1, 1, 7]
b=1

def remove_all(x, b):
	while b in x:
		x.remove(b)
remove_all(x,b)
print (x)
# Prints: [3, 2, 5, 7]

#C ---------------------------------------------------------
z = [1, 2, 4, 2, 1]
x = 1
y = 5


def add_this_many(x, y, temp):
	a = 0
	temp = list(z)
	while x in temp:
		temp.remove(x)
		a = a + 1
	while a != 0:
		z.append(y)
		a = a - 1
	
add_this_many(x,y,z)
print (z)

#D:--------------------------------------------------------
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print (a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

#E:--------------------------------------------------------
x = [3, 2, 4, 5, 1]

def reverse(x):
	x.reverse()
reverse(x)
print (x)
# Prints: [1, 5, 4, 2, 3]

#F:--------------------------------------------------------
x = [1, 2, 3, 4, 5]
n = [0] * 5

def rotate(x, k):
	c = 0
	c2 = 0
	k = k -1
	temp = list (x)
	while k <= len(x) - 1:
		n[c] = x[k]
		k = k + 1
		c = c + 1
	while c2 <= 1:
		n[c] = x[c2]
		c2 = c2 + 1
		c = c + 1
		

rotate (x,3) 
print (n)
#Prints: [3, 4, 5, 1, 2]

#H:--------------------------------------------------------
print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, ('eli manning', 'giants'): 2, 'joe montana': 4}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', 'joe flacco': 1, 'tom brady': 3, 'peyton manning': 1, 'joe montana': 4}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {'joe flacco': 1, 'peyton manning': 1, ('eli manning', 'giants'): 5, 'joe montana': 4, 'tom brady': 3}

superbowls[('steelers', '49ers')] = 11
print(superbowls)
#Prints: {'joe flacco': 1, ('steelers', '49ers'): 11, 'tom brady': 3, 'joe montana': 4, 'peyton manning': 1}

#I:--------------------------------------------------------


#J:--------------------------------------------------------
