####################################################
# Objects of different classes can share the same 
# method name and then call them from the same place 
# but applied to different objects.

# Example:
# The built-in function in Python len() has a polymorphic 
# behavior, since it calculates the length of an object 
# based on its type (strings, lists, tuples, among others), 
# returning the number of items or characters that compose it.

class Cow:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} say Moooo !!!")

class Sheep:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} say Beeee !!!")

cow1 = Cow("Lola")
sheep1 = Sheep("Cloud")

cow1.speak()
sheep1.speak()

animals = [cow1,sheep1]	
for animal in animals:
    animal.speak()

def animal_speak(animal):
    animal.speak()

animal_speak(cow1)
animal_speak(sheep1)