### Omar Trejo
### When should we use inheritance?

One common use of inheritance is to represent a hierarchical relationship between two or
more classes – one class is a more specific version of the other class. For example, dogs
are a specific type of pet, and a pet is a specific type of animal.

Using inheritance, here is a second attempt at representing dogs.

```python
class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(’...’)
        
class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print(’woof!’)
```

Notice that, by using inheritance, we did not have to redefine `self.name`, `self.owner`,
or the `eat` method. We did, however, redefine the talk method in the `Dog` class. In this
case, we want `Dogs` to `talk` differently, so we override the method.

The line `Pet. init (self, name, owner)` in the `Dog` class is necessary for inheriting
the instance attributes `self.is_alive`, `self.name`, and `self.owner`. Without
this line,`Dog` will never inherit those instance attributes. Notice that when we call
`Pet__init__`, we need to pass in `self`, since `Pet` is a class, not an instance.

### Questions

***1.*** Implement the `Cat` class by inheriting from the `Pet` class. Make sure to use superclass
methods wherever possible. In addition, add a `lose_life` method to the `Cat` class.

```python
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
    
    
    
    
    def talk(self):
        """A cat says meow! when asked to talk."""
        
        
        
        
    def lose_life(self):
        """A cat can only lose a life if they have at least
        one life. When lives reach zero, the ’is_alive’
        variable becomes False.
        """
        
        
```
-----

### Answer 1

```python

class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		Pet.__init__(self, name, owner)
		self.lives = lives
	
	def talk(self):
		print ('Meow!')
	
	def lose_life(self):
		self.lives -= 1
		if self.lives > 0:
			self.is_alive = True
		else:
			self.is_alive = False
```

-----

***2.*** Assume these commands are entered in order. What would Python output?

```python
class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)
        
class Bar(Foo):
    a = 1
    def baz(self, val):
        return val
        
f = Foo(4)
b = Bar(3)
print(f.a)
# prints what ?

print(b.a)
# prints what ?

print(f.garply())
# prints what ?

print(b.garply())
# prints what ?

b.a = 9
print(b.garply())
# prints what ?

f.baz = lambda val: val * val
print(f.garply())
# prints what ?
```
-----

### Answer 2

```python

f = Foo(4)
b = Bar(3)
print(f.a)
# Prints: 4

print(b.a)
# Prints: 3

print(f.garply())
# Prints: Call will errors since Foo does not inherit from Boo. Foo does not in turn have baz defined.

print(b.garply())
# Prints: 3

b.a = 9
print(b.garply())
# Prints: 9

f.baz = lambda val: val * val
print(f.garply())
# Prints: 16

```

-----
