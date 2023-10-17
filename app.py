from animal import Sheep,Cattle,Dog
from compartment import AnimalCompartment
from ranch import AnimalRanch


sheep_compartment = AnimalCompartment('Sheep comartment','sheep',5)
dog_compartment = AnimalCompartment('Dog compartment','dog',10)

sheep1 = Sheep('Dolly 1','white','Dorper')
sheep2 = Sheep('Dolly 2','white','Dorper')
sheep3 = Sheep('Dolly 3','white','Dorper')
sheep4 = Sheep('Dolly 4','white','Dorper')
sheep5 = Sheep('Dolly 5','white','Dorper')
sheep6 = Sheep('Dolly 6','white','Dorper')
sheep_compartment.add_animals([sheep1,sheep2,sheep3,sheep4,sheep5])
sheep_compartment.feed_animals("Oboke")
dog_compartment.feed_animals("Ring'o")