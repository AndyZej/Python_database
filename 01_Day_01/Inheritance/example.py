class Animal:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self):
        print("Hello " + self.name)



class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age


class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color


class Fish(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class Lion(Cat):
    def __init__(self, name: str):
        super().__init__(name, "hnedy")

    def say_hello(self):
        Animal.say_hello(self)
        print("Hello Iam the king of the Jungle")


dog = Dog("Dunco", 10)
dog.say_hello()

cat = Cat("Julian", color="red")

lion = Lion("Lion")
lion.say_hello()
print(type(lion))
print(isinstance(lion, Animal))
print(Lion.__mro__)

lion.say_hello()
cat.say_hello()