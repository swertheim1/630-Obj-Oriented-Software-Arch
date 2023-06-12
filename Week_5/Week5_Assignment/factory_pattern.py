""" Factory Pattern

Encapsulates """

from abc import ABCMeta, abstractmethod
from random import randint


class IPet(metaclass=ABCMeta):
    """ Pet Interface"""
    @abstractmethod
    def get_animal(self):
        pass


class Dog(IPet):
    def __init__(self):
        self.name = 'Max'
        self.sound = 'bark'
        self.age = 1

    def get_animal(self):
        return {"name": self.name, "sound": self.sound, 'age': self.age}


class Cat(IPet):
    def __init__(self):
        self.name = 'Ozzy'
        self.sound = 'meow'
        self.age = 12

    def get_animal(self):
        return {"name": self.name, "sound": self.sound, 'age': self.age}


class Ferret(IPet):
    def __init__(self):
        self.name = 'Noodle'
        self.sound = 'hiss'
        self.age = 3

    def get_animal(self):
        return {"name": self.name, "sound": self.sound, 'age': self.age}


class AnimalFactory:
    @staticmethod
    def get_animal():
        random_number = randint(0, 2)
        if random_number == 0:
            return Dog()
        elif random_number == 1:
            return Cat()
        elif random_number == 2:
            return Ferret()
        else:
            return 'Animal not available'


if __name__ == '__main__':
    animal = AnimalFactory.get_animal()
    print(animal.get_animal())
    animal = AnimalFactory.get_animal()
    print(animal.get_animal())
    animal = AnimalFactory.get_animal()
    print(animal.get_animal())
