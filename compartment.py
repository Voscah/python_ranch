"""COMPARTMENT CLASS FILE"""
from time import sleep
class AnimalCompartment:
    def __init__(self,name,label,capacity=10) -> None:
        self.name = name
        self.label=label
        self.capacity=capacity
        self.animals=[]
    def add_animal(self,animal):
        if (self.__is_empty__() or not self.__is_full__()):
            if self.label==animal.label:
                self.animals.append(animal)
            else:
                print(f"{animal.name} of label cannot be added to non matching compartment of label: {self.label}")
        else:
            print("Looks like compartment is already full")
    def increase_capcity(self,increment_amount=1):
        self.capacity+=increment_amount

    def __is_full__(self):
        return self.capacity==len(self.animals)
    def __is_empty__(self):
        return self.animals_in_compartment()==0

    def has_animals(self):
        return not self.__is_empty__()
    def feed_animals(self,food):
        if self.has_animals():
            # [print(animal.eat(food)) for animal in self.animals]
            for animal in self.animals:
                print("\nNow feeding {}".format(animal.name).center(20,"*"))
                animal.eat(food)
                sleep(2)
        else:
            print("No animals to feed")
    def add_animals(self,animals=[]):
        if len(animals)>0:
            for animal in animals:
                self.add_animal(animal)
        else:
            print("No animal to add")
    def animals_in_compartment(self):
        return len(self.animals)
