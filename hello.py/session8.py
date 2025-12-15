class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print("Some generic animal sound")
    
#task 1
class Mammals(Animal):
    def __init__(self, name, species, age,fur_colour,sound):
        super().__init__(name, species, age)
        self.fur_colour = fur_colour
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} is a Mammal and  make {self.sound}")

class Birds(Animal):
    def __init__(self, name, species, age,wing_span,sound):
        super().__init__(name, species, age)
        self.wing_span = wing_span
        self.sound = sound
        
    def make_sound(self):
        print(f"{self.name} is a bird and  make {self.sound} ")
class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self,animal):
        self.animals.append(animal)
    def show_all(self):
        for a in self.animals:
            print(f"{a.name} speices : {a.species}")

class Keeper():
    def __init__(self,name):
        self.name = name

    def feed_all(self,zoo):
        for i in zoo.animals:
            print(f'{self.name} feeding {i.name}')


Cow = Mammals('Cow','Red-Bull',3,'Red','hamba-hamba')
Cow.make_sound()
Parrot =Birds('Rose','Chinese',2,6,'chickir chikir')
Parrot.make_sound()

zoo_animal = Zoo()
zoo_animal.add_animal(Cow)
zoo_animal.add_animal(Parrot)

for a in zoo_animal.animals:    
    a.make_sound()

keeper_haren_ken = Keeper('haren ken')
keeper_haren_ken.feed_all(zoo_animal)
zoo_animal.show_all()