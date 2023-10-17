"""ANIMAL CLASS FILE"""
from datetime import datetime
class Animal:
    """
    Animal class will have the following attributes:
    - name
    - color
    - breed
    - label
    Methods:
    - eat(food)->None
    - cry()-> None
    - walk()-> None
    - breath()-> None
    """
    def __init__(self,name,color,breed,label) -> None:
        self._name = name
        self._color= color
        self._breed=breed
        self._label = label
    # Name attribute
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    # Color attribute
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color
    # Breed attribute
    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self,breed):
        self._breed=breed
    # Label attribute
    @property
    def label(self):
        return self._label
    @label.setter
    def label(self,label):
        raise ValueError(f'{self.label} to {label} Cannot set label once initialized')
    def eat(self,food):
        print(f"{self.name} is eating {food}")
    def cry(self):
        pass
    def walk(self):
        print(f"{self.name} is walking")
    def breath(self):
        print(f"{self.name} is breating")

class Sheep(Animal):
    def __init__(self, name, color, breed) -> None:
        super().__init__(name, color, breed, "sheep")
    def eat(self, food):
        print('{} Sheep is eating {} at {}'.format(self.name,food,datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')))
class Dog(Animal):...
class Goat(Animal):...
class Cattle(Animal):...
class Chicken(Animal):...

# sheep1 = Sheep('Katolo','brown','dorper')
# dog1 = Dog('Simba','brown','local','dog')
# sheep1.eat('Grass')
# dog1.eat('Rabbit')