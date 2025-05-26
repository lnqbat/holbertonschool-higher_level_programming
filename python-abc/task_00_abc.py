from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Defines an animal.
    """
    @abstractmethod
    def sound(self):
        """
        Define the sound an animal makes.
        """
        pass

class Dog(Animal):
    """
    Defines a dog.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Defines a cat.
    """
    def sound(self):
        return "Meow"
