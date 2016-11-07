# Study Guide

##Q:

### Color Class

- Create a class called "Color" that will store a tuple of (r,g,b). 
- The tuple should be stored in a data member called color.
- The components of the color tuple should be stored in data members: red, green, blue as well 
- Add a __str__ method to print out the color class so it looks like: "(red: redVal, green: greenVal, blue: blueVal)"
- Here is some usage:

```python

c1 = Color((255,0,0))
print(c1.red)
#prints: 255

c1.blue = 255
print(c1)
#prints: (red: 255, green: 0, blue: 255)

c1.setColor((0,0,0))
print(c1)
#prints: (red: 0, green: 0, blue: 0)

```
##A:
```python
class Color(object):
	def __init__(self,red = 0,blue = 0,green =0):
		if type(red) is tuple:
			self.setColor(*red)
		self.setColor(red,blue,green)
		
	def __str__(self):
		return "(red: %s, green: %s, blue: %s)" % (self.red,self.green,self.blue)
	
	def setColor(self, red = 0, green = 0, blue = 0):
		if type(red) is tuple:
			self.setColor(*red)
		else:
			self.red = red
			self.green = green
			self.blue = blue
```
----

##Q:

Overload the addition operator so that we can add two colors. Adding colors is a pretty wierd experience, so we will create our own addition method. Basically we will average each color. 

For example:

```python

c1 = Color(255,255,255)
c2 = Color(0,0,0)
c3 = c1 + c2

print(c3)
#prints: (red: 128,green: 128,blue: 128)
```

##A:
```python
class Color(object):
	def __init__(self,red = 0,blue = 0,green =0):
		if type(red) is tuple:
			self.setColor(*red)
		self.setColor(red,blue,green)
		
	def __str__(self):
		return "(red: %s, green: %s, blue: %s)" % (self.red,self.green,self.blue)
	
	def setColor(self, red = 0, green = 0, blue = 0):
		if type(red) is tuple:
			self.setColor(*red)
		else:
			self.red = red
			self.green = green
			self.blue = blue
			
	def __add__(self, x):
		if type(x) is tuple:
			self.setColor(*x)
		newR = (self.red + x.red) // 2
		newG = (self.green + x.green) // 2
		newB = (self.blue + x.blue) // 2
		return (newR,newG,newB)
```
----

##Q:

### Grayscale Class

This class will ***extend*** the color class.

So what is gray scale? Its where you take the 3 individual parts of a color and using those values you calculate a single value that will be assigned to each of the 3 components, making it some shade of gray.
 
For example here is red: `(0,255,0)` and here is the gray scale equivalent: `(85,85,85)` (using the average method from below).

Your `GrayScaler` class is serious about its grayscalin` powers and has three methods to turn a color into its monochromatic equivalent:
- lightness
- average
- luminosity
- custom

**Lightness**

The lightness method averages the most prominent and least prominent colors: `(max(R, G, B) + min(R, G, B)) / 2`.

**Average**

The average method simply averages the values: `(R + G + B) / 3`.

**Luminosity**

This method also averages the values, but it forms a weighted average to account for human perception. We’re more sensitive to green than other colors, so green is weighted most heavily. The formula for luminosity is `0.21 * R + 0.72 * G + 0.07 * B`

**Custom**

This method allows the user to pass in three floats to act as the weights in your formula: `w1 * R + w2 * G + w3 * B`

Here is some example usage to help you determine how to design your class:

```python

myColor = (255,0,0)
grayish = GrayScaler(myColor)
gray1 = grayish.Average()
gray2 = grayish.Custom(.33,.44,.23)


grayish2 = GrayScaler() # defaults to black in the class if no color provided
grayish2.SetColor(255,192,203)
gray3 = grayish2.Luminosity()
```

```python
"""
@Description: Gets an RGB color represented as a tuple, and converts it to a 
				gray scale equivalent based on chosen method.
@Methods:
    Lightness - as described above
    Average - as described above
    Luminosity - as described above
    Custom - as described above
    SetColor - Lets user change the color originally passed in.
"""
class GrayScaler(Color):
```

##A:
```python
class GrayScaler(Color):
	def __init__(self, red = 0, green = 0, blue = 0):
		Color.__init__(self, red, green, blue)
	
	def Lightness(self):
		x = [self.red, self.green, self.blue]
		light = (min(x) + max(x)) // 2
		maxIndex = x.index(max(x))
		if maxIndex == 0:
			return (self.red,light,light)
		elif maxIndex == 1:
			return (light,self.green,light)
		elif maxIndex == 2:
			return (light,light,self.blue)
			
	def Average(self):
		avg = (self.red + self.green + self.blue) // 3
		return (avg,avg,avg)
	
	def Luminosity(self):
		lum = int(self.red*.21 + self.green*.72 + self.blue*.07)
		return (lum,lum,lum)
		
	def Custom(self,r, g, b):
		custom = int(self.red*r + self.green*g + self.blue*b)
		return (custom,custom,custom)
```
----

## Q:

Create a point class, line class, and a rectangle class. 

- A point is a tuple of two integers: (3,6)
- A line consists of two points: (3,6),(7,8)
    - Add a length method 
- A rectangle consists of two points as well, the upper right, and the lower left.
    - Add an area and perimeter method

##A:
```python
import math

class point(object):
	def __init__(self, x1 = None, y1 = None, x2 = None, y2 = None):
		if type(x1) is tuple and type(y1) is tuple:
			self.explode(*x1, *y1)
		else:
			self.x1 = x1
			self.y1 = y1
			self.x2 = x2
			self.y2 = y2
		
	def explode(self, x1 = None, y1 = None, x2 = None, y2 = None):
		point.__init__(self, x1, y1, x2, y2)

	
class line(point):
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.setXY(*p1,*p2)
		
	def setXY(self, x1 , y1 , x2, y2 ):
		point.__init__(self, x1 , y1 , x2, y2)
	
	def length(self):
		l = math.hypot(self.x2 - self.x1, self.y2 - self.y1)
		return l
	
class rectangle(point):
	def __init__(self, p1, p2):
		point.__init__(self, p1, p2)
		self.l = self.x2 - self.x1
		self.w = self.y2 - self.y1
	def area(self):
		return abs(self.l*self.w)
	def perimeter(self):
		return 2*(self.l+self.w)
	
p1 = (0,0)
p2 = (3,4)

b = line (p1,p2)
print (b.length())
# Prints: 5.0
c = rectangle (p1,p2)
print (c.area())
# Prints: 12
print (c.perimeter())
# Prints: 14
```
----

## Q:

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_old(self):
        return self.age > 40

        
person = Person('G. H. Hardy', 70)  
print person.is_old() # Prints True
```

Write a `Student` class that extends the `Person` class and add a method: `is_honor_student` that would print `True` if the students gpa is greater than 3.0

```python
student = Student('G. H. Hardy', 70, 4.0)
print student.is_old()	# prints True
print student.is_honor_student()	# prints True
```

##A:
```python
class Student(Person):
	def __init__(self, name, age, gpa):
		Person.__init__(self, name, age)
		self.gpa = gpa
		
	def is_honor_student(self):
		return self.gpa > 3.0
```
----

## Q:

Run a binary search on the following values looking for key=55. Show the index values for `first` `mid` and `last` at each iteration.

| 0  | 1 |2 | 3  |  4|  5	|  6	|7|  8	| 9 	|  10	|  
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 5 | 13| 19 | 22	| 41	| 55	| 68	| 72	| 81	| 98 |


##A:
```python
x = {0:0,1:5,2:13,3:19,4:22,5:41,6:55,7:68,8:72,9:81,10:98}

f = 0
l = len(x)
m = (f+l) // 2
key = 55

found = False

for k,v in x.items():
	while not found:
		if x[m] == key:
			found = True
			print (m,x[m])
		if key > x[m]:
			f = m
		else:
			l = m
		m = (f+l) // 2
```
----

## Q:

Write a function that removes all instances of an element from a list.

```python
def remove_all(el, lst):
"""Removes all instances of el from lst.
>>> x = [3, 1, 2, 1, 5, 1, 1, 7]
>>> remove_all(1, x)
>>> x
[3, 2, 5, 7]
"""
```
##A:
```python
def remove_all(el, lst):
	for i in lst:
		lst.remove(el)
	return lst
```
----

## Q: 

Given a list of words like so:

```python 
words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]
```

Write a python snippet to find the words that occur most often. You output should look something like the following: 

```python
[('eyes', 8), ('the', 5), ('look', 4)]
```
##A:
```python
def frequency(lst):
	frequency = {}
	for word in lst:
		if word not in frequency:
			frequency[word] = 1
		else:
			frequency[word] = frequency.get(word)+1
	return frequency

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

print (frequency(words))
# Prints: {'look': 4, 'under': 1, 'my': 3, "don't": 1, 'not': 1, "you're": 1, 'eyes': 8, 'around': 2, 'the': 5, 'into': 3}
```
----

## Q:

Write a class called `book_analysis` that will do a word frequency analysis on a book. You can assume that the book has had all punctuation removed. Your class should count the number of unique words and be able to return the **n**<sup>th</sup> most frequent word. Below is some code that WILL actually do what I'm asking you to do (but not in a class).

```python
import string
import operator

#url for book = http://www.gutenberg.org/files/2701/2701.txt
#go to url and save book as moby_dick.txt on your computer
f = open('moby_dick.txt')


dict = {}

for line in f:
    exclude = set(string.punctuation)
    words = ''.join(ch for ch in line.strip() if ch not in exclude).lower()
    for word in words.split(' '):
        if not word in dict:
            dict[word] = 0
        dict[word] += 1

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_dict)
```

The `sorted_dict` looks like:

```

[('the', 14508), ('of', 6701), ('and', 6434), ('a', 4690), ('to', 4658), ('in', 4202), ('', 3491), ('that', 2955), ('his', 2520), ('it',2382), ('i', 1943), ('but', 1781), ('with', 1768), ('he', 1749), ('is', 1731), ('as', 1730), ('was', 1637), ('for', 1627), ('all', 1493),('this', 1411), ('at', 1326), ('by', 1219), .... ('repute', 1), ('aftman', 1), ('incredibly', 1), ('flexion', 1), ('shakespeares', 1), ('coursefor', 1), ('scabbards', 1), ('causesuch', 1), ('filial', 1), ('barwait', 1), ('hornsofplenty', 1), ('sash', 1), ('races', 1), ('linenow', 1), ('andromedaindeed', 1)]
```
where the word and occurence are in a tuple.

Your job is to organize into class form. Lets assume the constructor will load the book. Here is some usage:

```python
anlyz = BookAnalysis('moby_dick.txt')
most = anlyz.getnth(3)
print(most)
# ('and', 6434)
x = anlyz.occurs('barwait')
print(x)
# barwait occurs 1 times
print(anlyz.totalWords())
# total words: 20211
```

Some of the methods return a printed message (e.g. "barwait occurs 1 times"), this is ok for this test problem, but normally methods do not print messages and return values!
##A:
```python

```
----

## Binary Search Example:
```python
import random

nums = []

for i in range(100):
	nums.append(random.randint(0,500))

searchKey = random.randint(1,100)
print(searchKey)

nums.append(searchKey)

nums = sorted(nums)

print(nums)

f = 0 
l = len(nums)
m = (f + l) // 2



Found = False

while not Found:
	if nums[m] == searchKey:
		Found = True
		print(m)
	if searchKey > nums[m]:
		f = m 
	else:
		l = m 
		
	m = (f + l) // 2
	
```
