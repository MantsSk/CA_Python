from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "Miau"


class Dog(Animal):

    def make_sound(self):
        return "Woof"


class CatDog(Cat, Dog):
    pass


class CatDog(Animal):
    def make_sound(self):
        a = Cat()
        b = Dog()
        print(f"{a.make_sound()}{b.make_sound()}")

katasunis = CatDog()
# What sound will it make?
katasunis.make_sound()
