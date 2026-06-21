# interface, abstract, enum

from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    RED = "#1111"
    GREEN = "#222"
    BLUE = "#2222"


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass



class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print("foo")

    @abstractmethod
    def move(self):
        # raise NotImplementedError()
        pass


class Dog(Animal, Swimmable):
    def __init__(self, name, age, color: Color):
        super().__init__(name, age)
        self.color = color

    def move(self):
        print("som pes a beham")

    def swim(self):
        print("som pes a viem aj plavat")


dog = Dog("Dog", 22, Color.RED)

animals: list[Animal] = [dog]

for animal in animals:
    print(animal.name)
    animal.move()

print()
print(dog.color)
print(dog.color.value)