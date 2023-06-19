####################################################
# Minimal class definition
class BasicBird:
    pass

myBird = BasicBird()
myBird2 = BasicBird()
myBird3 = BasicBird()
print(type(myBird))
print(myBird)
print(myBird3)
print(myBird3)
print('Different ID means different object')
print('====================================')

####################################################
# More complex classes definitions
# Attributes
class Bird:
    # Attribute for all objects
    wings = True

    # Constructor that recieives the colour of the bird
    # self means the current object
    ## "__" means private
    def __init__(self,colour,species) :
        self.colour = colour
        self.species = species
        self.other_attribute = colour

myBird = Bird('red','tucan')
print(myBird.colour)
print(myBird.other_attribute)
print(Bird.wings)
print(myBird.wings)
print('====================================')
# Methods

class Bird:
    # Attribute for all objects
    wings = True

    # Constructor that recieives the colour of the bird
    # self means the current object
    def __init__(self,colour,species) :
        self.colour = colour
        self.species = species
    
    def tweeet(self):
        print(f'Tweeet like a {self.colour} bird')
    def fly(self,meters):
        print(f'Flying {meters} meters')	
 

tweety = Bird('red','tucan')
print(tweety.colour)
print(tweety.wings)
tweety.tweeet()
tweety.fly(100)
print('====================================')
####################################################
# Decorators

# Instance method:
# Seen so far. When created, they can access and modify the components of the class.

# Class method:
# @classmethod, not attached to instances, but to the class itself, cannot access instance attributes. They take the cls parameter

# Static methods:
# @staticmethods, It does not modify either the class or the instance.

class Bird:
    # Attribute for all objects
    wings = True

    # Constructor that recieives the colour of the bird
    # self means the current object
    def __init__(self,colour,species) :
        self.colour = colour
        self.species = species
    # Instance method
    def tweet(self):
        print(f'Tweet like a {self.colour} bird')
    def fly(self,meters):
        print(f'Flying {meters} meters')	
    def paint_in_black(self):
        self.colour = 'black'
        print(f'Painted in black')
        self.tweet()
    # Class method
    @classmethod #cls means the class itself
    def lay_eggs(cls,num):
        print(f'laying {num} eggs')
        print(cls.wings)
        # does not have access to self
        # but can access cls attributes
    # Static method
    @staticmethod
    def see():
        # does not have access to self or cls
        print('The bird sees')

myBird = Bird('red','tucan')
myBird.wings = False
print(myBird.wings)
print(Bird.wings)
myBird.paint_in_black()
Bird.lay_eggs(10)
# Bird.fly(100) This would be a mistake, this is an instance method
myBird.lay_eggs(10)
Bird.see()
print('====================================')

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo=True

p = Jugador()
print(p.vivo)
p.revivir()
print(p.vivo)