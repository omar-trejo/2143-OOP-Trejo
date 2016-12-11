## Test 1 Study Guide
======
#### Python Container Types
Give a basic overview of each data type below. What kind of data could/would you store in each? Are each of them `mutable`? Give examples of each.
- lists 
- dictionary's
- tuples

======
#### Definitions

- Attributes:
	The data within an object. This data represents the objects "state" and is typically the subject of an objects methods (meaning the methods can be used to change the values within the attributes thereby changing the "state" of the object).

- Class:
	A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

- Constructor:
	It is a special type of subroutine called to create an object. It prepares the new object for use, often accepting arguments that the constructor uses to set required member variables.

- Data Member:
	A class variable or instance variable that holds data associated with a class and its objects.

- Encapsulation:
	In programming languages, encapsulation is used to refer to one of two related but distinct notions, and sometimes to the combination thereof:
		- A language mechanism for restricting access to some of the object's components.
		- A language construct that facilitates the bundling of data with the methods (or other functions) operating on that data.

- Immutable:
	Is an object whose state cannot be modified after it is created.

- Information Hiding:
	This is a type of encapsulation can be used to hide data members and members function... Under this definition, encapsulation means that the internal representation of an object is generally hidden from view outside of the object's definition. Typically, only the object's own methods can directly inspect or manipulate its fields.

- Inheritance:
	The transfer of the characteristics of a class to other classes that are derived from it.

- Instance Variable:
	An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

- Method:
	A special kind of function that is defined in a class definition.

- Mutable:
	An object which can be modified after it is created.

======
#### Q: Looping over Lists

Given the following list: `[34,55,3,22,"hello","wassup",99,17.9,42]` provide more than one 
method for accessing each element (in this example, by access I mean print). 

#### A:
```python
a = [34,55,3,22,"hello","wassup",99,17.9,42]

# ----------------Method 1----------------
for i in a:
  print (i)

# ----------------Method 2----------------
for i in range(len(a)):
  print (a[i])
  
# Both Print: 34
			  55
			  3
			  22
			  hello
			  wassup
			  99
			  17.9
			  42
```
=====

#### Q: Looping over Dictionaries

Given the following dictionary: {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7'}

Loop over "it" and print out the key value pairs.

#### A:
```python
a =  {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7'}

for k,v in a.items():
  print (k,v)

# Prints: e 5
          a 1
          f 6
          d 4
          c 3
          b 2
          g 7
```

=====

#### Q: Writing Functions

A clerk works in a store where the cost of each item is a positive integer number of dollars.
So, for example, something might cost $21, but nothing costs $9.99. In order to make change
a clerk has an unbounded number of bills in each of of the following denominations: $1, $2,
$5, $10, and $20. Write a procedure that takes two arguments, the cost of an item and the
amount paid, and prints how to make change using the smallest possible number of bills.

#### A:
```python
class reg(object):
	def __init__(self,paid=None,cost=None):
		self.paid=paid
		self.cost=cost
		self.tw = 0
		self.tn = 0
		self.fv = 0
		self.two = 0
		self.one = 0
	
	def __str__(self):
		return "Paid: %s, Cost: %s, Change: $20:%s, $10:%s, $5:%s, $2:%s, $1:%s" % (self.paid, self.cost, self.tw, self.tn, self.fv, self.two, self.one)
		
	def getChange(self):
		change = self.paid - self.cost
		while change >= 20:
			change = change - 20
			self.tw = self.tw + 1
		while change >= 10:
			change = change - 10
			self.tn = self.tn + 1
		while change >= 5:
			change = change - 5
			self.fv = self.fv + 1
		while change >= 2:
			change = change - 2
			self.two = self.two + 1
		while change >= 1:
			change = change - 1
			self.one = self.one + 1
			
a=reg(71,20)
a.getChange()
print(a)

# Prints: Paid: 71, Cost: 20, Change: $20:2, $10:1, $5:0, $2:0, $1:1
```

=====
#### Q: Working With Lists

Write a procedure that takes a string of words separated by spaces (assume no punctuation
or capitalization), together with a ”target” word, and shows the position of the target word
in the string of words. 

For example, if the string is:
```
we dont need no education we dont need no thought control no we dont
```

and the target is the word `dont` then your procedure should return the list `1, 6, 13` because
`dont` appears at the `1st, 6th, and 13th` position in the string. Your procedure should return 
`False` if the target word doesn’t appear in the string.

#### A:
```python
def position(target):
  a = "we dont need no education we dont need no thought control no we dont"
  x = a.split()
  
  target = target
  p = []
  
  if target not in x:
    return False

  for position, word in enumerate(x):
    if word == target:
      p.append(position)
  
  return p
    
  
print (position('dont'))
# Prints: [1, 6, 13]

print (position('test'))
# Prints: False
```
=====
#### Choosing Correct Data Type

Create a data structure to hold data for a student. This structure would hold the following:
`string` first_name, `string` last_name, `int` id, `string` dob 

=====

#### Q: Stats Function

Write a function that will return a `tuple` that contains the `average`, `maximum`, and the `minimum` number in a given list of integers.

#### A:
```python
def min_max_avg(list):
  return ((min(list),max(list),sum(list)/len(list)))
  
l1 = [3,4,5,2,33,77,65,67,22,12,3,44,5,66,77]
print (min_max_avg(l1))
```

=====

#### Q: Stats Class

Now take that function with the logic you just created to solve the problem above and turn it into a class. Your class will be called `listStats` and have the following methods:

- setList()
- getMin()
- getAvg()
- getMax()

Here is some example usage of your class:

```python
l1 = [3,4,5,2,33,77,65,67,22,12,3,44,5,66,77]
l2 = [55,7,66,23,45,3,4,11,2,99,8,7,98,58,23]
s1 = listStats(l1)
print(s1.getAvg()) 
s1.setList(l2)
print(s1.getMax())
```
####A:
```python
class listStats(object):
  def __init__(self, list):
    self.setList(list)
    self.min, self.max, self.avg = None, None, None
    
  def __str__(self):
    return "%s" % (self.list)
  
  def setList(self,list):
    self.list = list
    
  def getMin(self):
    self.min = (min(self.list))
    
  def getAvg(self):
    self.avg = (sum(self.list)/len(self.list))
    return self.avg
    
  def getMax(self):
    self.max = (max(self.list))
    return self.max
    
#-----------------------------------------------
l1 = [3,4,5,2,33,77,65,67,22,12,3,44,5,66,77]
l2 = [55,7,66,23,45,3,4,11,2,99,8,7,98,58,23]
s1 = listStats(l1)
print(s1.getAvg()) 
s1.setList(l2)
print(s1.getMax())

```
=====
#### Q: String Output of a Class

Given the following class:

```python
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self,x=0,y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y
```

Write a `str` method to print out the string representation of the class. Example output:
```python
p1 = Point(3,5)
print(p1)
# prints: (x:3,y:5)
```

#### A:
```python
class Point:
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y
    
  def __str__(self):
    return "(x:%s,y:%s)" % (self.x, self.y)
        
p1 = Point(3,5)
print(p1)

# Prints: (x:3,y:5)
```

=====

#### Q: Overloading an Operator

Given the following example of how to overload an operator:
```python
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    #Looks like an answer to another question!!! ;)
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
        # or
        # return "(%d , %d)" % (self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
```
And it's usage:

```python
p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)
# prints: (1,5)
```
Overload the `equal` operator to test for `point` equality.

#### A:
```python
class Point(object):
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y
  def __eq__(self,other):
    if (self.x,self.y) == (other.x,other.y):
      return True
    else:
      return False
	  
p1 = Point(2,3)
p2 = Point(-1,2)

print (p1 == p2)
# Prints: False
```
======

#### Dictionary Class

Write a class called `wordDictonary` that represents an actual dictionary. Your class should contain the following methods:
- `loadDictionary` : 
    - reads a file that contains `word: definition` 
    - a word may occur more than once (same word alternate definition)
    - you should be able to hold all definitions
- `updateDictionary`:
    - a method that lets you add a word:definition to the class
- `findWord`:
    - this method receives a word, and returns all definitions that correspond to it. 
- `removeWord`:
    - this method lets you remove a word from the dictionary. 
    
#### A:
```python
class wordDictonary(object):
	def __init__(self):
		self.dict = {}
		
	def __str__(self):
		string = ''
		for k,v in self.dict.items():
			string += k + ":"
			for wd in v:
				string += "\n\t"
				string += ''.join(wd)
				
			string += "\n"
		return string
		
	def loadDictionary(self):
		pass
	
	def updateDictionary(self,word,definition):
		if not word in self.dict:
			self.dict[word] = []
		self.dict[word].append(definition)
		
	def findWord(self,word):
		if word in self.dict:
			return self.dict[word]
		else:
			return None
	
	def removeWord(self,word):
		if word in self.dict:
			del self.dict[word]
			
			
wd = wordDictonary()
wd.updateDictionary('run','go fast')
wd.updateDictionary('run','move legs powerfully')
wd.updateDictionary('walk','go slow')
wd.updateDictionary('walk','not run')


print(wd)

# Prints: run:
			   go fast
			   move legs powerfully
		  walk:
			   go slow
			  not run
```
======

#### Q: Median Trickery

- Complete the function using this algorithm: 
    - continually remove the largest and smallest values from the list and return either the last value (if there is only one left) or the average of the two last values (if there are two left).
    - Do not sort the list, and don't use any for loops in your solution.
    - Functions `max` and `min` may be helpful, as well as one or more list methods.

```python
def myMedian(L):
""" 
@Description: Return the median of the numbers in L.
@Params: L (list)
@Returns: median (int)
"""
	# Start with a copy of the list so we don’t modify the original.
	L = L[:]
```
#### A: 
```python
def myMedian(list):
  x = list
  median = None
  
  while len(x) > 2:
    x.remove(min(x))
    x.remove(max(x))
  
  if len(x) == 2:
    return sum(x)/2
  
  return x[0]
  
list = [1,3,4,5,10,7,8]

print (sorted(list))
print (myMedian(list))

# Prints: [1, 3, 4, 5, 7, 8, 10]
#		  5
```
