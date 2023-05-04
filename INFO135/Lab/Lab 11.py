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

    @abstractmethod
    def print_info(self):
        pass

class Mammal(Animal):
    skin = 'hair'
    def __init__(self, name, species, carnivorous=None):
        super().__init__(name, species)
        self.carnivorous = carnivorous

    def speak(self):
        print('i mammal haha')

    def print_info(self):
        print(f'Name: {self.name}, Species: {self.species}, Carnivorous: {self.carnivorous}, Skin: {self.skin}')

class Reptile(Animal):
    skin = 'scale'
    def __init__(self, name, species, carnivorous=None, bite=None):
        super().__init__(name, species)
        self.carnivorous = carnivorous
        self.bite = bite

    def speak(self):
        print('i reptile yesyes')

    def print_info(self):
        pass


class Bird(Animal):
    skin = 'feathers'
    carnivorous = False
    def __init__(self, name, species, flight=None):
        super().__init__(name, species)
        self.flight = flight

    def speak(self):
        print(' i bird yesyes')

    def print_info(self):
        pass

class Enclosure:
    animals = []

    def __init__(self, id):
        self.id = id

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Added {animal.name} to {self.id}')

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

mammal1.print_info()