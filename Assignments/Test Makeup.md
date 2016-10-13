# Omar Trejo
-----

## 1: Definitions: 

Using python comments, label all lines that an OOP definition could be applied to.

```python

class Employee:

   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)

emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount


```
-----

### Answer 1

```python

class Employee:                      #Class

   empCount = 0                      #Class Variable

   def __init__(self, name, salary): #Constructor
      self.name = name               #Data Member
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):           #Method
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zara", 2000)        #Instance

emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount


```

-----

## 2: List Functions

Given the list below:

```python
States = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 'New Hampshire', 'Maine', 'Texas']
```

**A)** Sort the list

**B)** Add 'Oklahoma' to the list in alphabetical order without sorting the list again. Actually, write a function that would add an item to the list in alphabetical order. Example:

```python 
def addInOrder(L):
    #add to the list L in the proper order


    #return your ordered list
    return L
```
----
### Answer 2
```python

class lst(object):
	
	def __init__(self):
		self.states = ['Alabama','Illinois','Wyoming','New York', 'Vermont', 
		'New Hampshire', 'Maine', 'Texas']

	def addInOrder(self,n):
		x = self.states
		x.sort()
		p = 0
		for word in x:
			if n > word:
				p += 1
		x.insert(p,n)
		return x

a = lst()
print(a.addInOrder('Oklahoma'))

```

-----

## 3: Looping over Lists
(10 Points)

Using the following list as an example: `L = [10,20,30,40,50,60,70,80,90,100]` write a function that would divide each value by its index location + 1. Our example list would turn into: `L = [10,10,10,10,10,10,10,10,10,10]`. Remember NOT to get caught up on these values. Your function should work on any list.

Usage:
```python
L =  [10,20,30,40,50,60,70,80,90,100]
NList = addPrevious(L)
print(NList)
# prints: [10,10,10,10,10,10,10,10,10,10]
```

Your answer should consist of just the function definition and none of the usage I provided above.

```
-----

### Answer 3

```python

def divideList(l):
	n = []
	for x in range(len(l)):
		n.append(l[x]/(x+1))
	return n

```

-----

## 4: Looping over Dictionaries
(10 Points)

Given the following dictionary: 
```python
months = { 1 : "January", 
     	2 : "February", 
    	3 : "March", 
        4 : "April", 
     	5 : "May", 
     	6 : "June", 
    	7 : "July",
        8 : "August",
     	9 : "September", 
    	10 : "October", 
        11 : "November",
    	12 : "December" }
```
Iterate over this dictionary, and create a new one that only uses the first three letters of the month. Also make the new months all lowercase. Your new dictionary should look like:

```
abbr_months = {1:"jan",
        2 :"feb",
        3 :"mar",
        4 : "apr", 
     	5 : "may", 
     	6 : "jun", 
    	7 : "jul",
        8 : "aug",
     	9 : "sep", 
    	10 : "oct", 
        11 : "nov",
        12 : "dec" }
```

To help you look up `string slicing` and `lower`. 

Your answer should include just the code that loops and creates the new dictionary.

```
-----

### Answer 4

```python

def aMonths(d):
	n = {}
	for k,v in d.items():
		x = ''
		x = v.lower()[0]+v[1]+v[2]
		n[k]=x
	return n

```

-----

## 5: Min and Max
(10 Points)

- Assume that pythons built in min , max , and sort functions are broken. Write a function that receives a list then traverses the list and returns the `min` , `max`, and `average` values in a tuple.

```python
def miniStats(L):
""" 
@Description: Finds the min,max,and average values in a list
@Params: L (list)
@Returns: tuple (int,int,double)
"""
	# Start with a copy of the list so we don’t modify the original.
	L = L[:]



```

When writing your answer, include the entire function definition (without the comment block).

```
-----

### Answer 5

```python

def miniStats(l):
	l.sort()
	x = l
	min = x[0]
	max = x[(len(x)-1)]
	avg = sum(x)/len(x)
	return (min,max,avg)

```

-----

## 6: Prime Class


Write a class called `myPrimes` that represents a collection of your prime numbers. 
- `addPrime` : 
    - receives a prime number and adds it to your collection of primes
    - it must be checked to make sure it's prime! (should be a private method that does this).
- `removePrime`:
    - a method will remove a prime from your list
- `printPrimes`:
    - this method will print your prime numbers out 
 

```
-----

### Answer 6

```python

class prime(object):
	def __init__(self,prime = None):
		self.p = prime
		self.lst = []
	def addPrime(self,n):
		if n < 1:
			return False
		else: 
			for i in range(2,n):
				if n == 2:
					self.lst.append(n)
				if (n % i) == 0:
					return False
			else:
				self.lst.append(n)
	def removePrime(self):
		self.lst.pop()
	def __str__(self):
		return "%s" % (self.lst)

a = prime()

a.addPrime(3)
a.addPrime(3)
a.addPrime(7)
a.addPrime(49)
a.addPrime(2)
a.removePrime()

print(a)

```

-----
