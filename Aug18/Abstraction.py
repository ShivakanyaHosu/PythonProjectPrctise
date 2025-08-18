from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Bark bark")


obj_dog = Dog("shira")
obj_dog.make_sound()
