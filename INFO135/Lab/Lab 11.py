from abc import ABC, abstractmethod


class Animal(ABC):
    all_animals = []

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.alive = True
        Animal.all_animals.append(self)

    @abstractmethod
    def speak(self):
        pass


class Mammal(Animal):
    skin = 'hair'
    def __init__(self, name, species, diet=None):
        super().__init__(name, species)
        self.diet = diet  # False = Carnivore, True = Herbivore

    def speak(self):
        print('i mammal haha')


class Reptile(Animal):

    def __init__(self, name, species, diet=None, bite=None):
        super().__init__(name, species)
        self.diet = diet
        self.bite = bite
        self.skin = 'scales'

    def speak(self):
        print('i reptile yesyes')


class Bird(Animal):

    def __init__(self, name, species, flight=None):
        super().__init__(name, species)
        self.flight = flight
        self.diet = 'Herbivore'

    def speak(self):
        print(' i bird yesyes')


# Creates Animals
mammal1 = Mammal('Ferela', 'lion', True)
mammal2 = Mammal('Leatboon', 'lemur', False)
mammal3 = Mammal('Doonok', 'donkey', False)
mammal4 = Mammal('Lurtacar', 'lemur', False)
reptile1 = Reptile('Fereetteoci', 'frog', False, False)
reptile2 = Reptile('Snakossum', 'snake', True, True)
reptile3 = Reptile('Citigator', 'crocodile', False, True)
bird1 = Bird('Flautingo', 'flamingo', True)
bird2 = Bird('Malliceo', 'parrot', True)
bird3 = Bird('Tucoda', 'penguin', False)
