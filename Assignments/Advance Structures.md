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
