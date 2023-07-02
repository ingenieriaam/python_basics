####################################################
# 

class Animal:
    pass

class Bird(Animal):
    pass

print(Bird.__bases__)
print(Animal.__subclasses__())

#################################################

class Animal:
    def __init__(self,age,colour):
        self.age = age
        self.colour = colour
    def born(self):
        print("I've been born")

    def eat(self):
        print("I'm eating")

class Bird(Animal):
    pass

piolin = Bird(2,'yellow')
piolin.born()
print(piolin.colour)

#################################################
# extended inheritance

class Animal:
    def __init__(self,age,colour):
        self.age = age
        self.colour = colour
    def born(self):
        print("I've been born")

    def speak(self):
        print("I'm speaking")

class Bird(Animal):
    def __init__(self,age,colour,flying_height):
        # set attr of super class Animal
        super().__init__(age,colour) 
        self.flying_height = flying_height
    def speak(self):
        print("I say Pio")
    def fly(self,meters):
        print(f"I'm flying {meters} meters")

piolin = Bird(2,'yellow',30)
piolin.born()
print(piolin.colour)
piolin.speak() # i'm speaking like a bird



class Dad:
    def speak(self):
        print("I'm speaking")
class Mom:
    def laugh(self):
        print("Jajaja")
    def speak(self):
        print("How are you?")

class Son(Dad, Mom):
    pass

class Grandson(Son):
    pass

theGrandson = Grandson()
theGrandson.speak() # Corresponds to the order of inheritance
theGrandson.laugh()

print('====================================')

# Lection 7 example
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez,Mamifero,Reptil,Ave):
    pass
