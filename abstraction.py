from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def nourrir(self):
        pass

class Panda(Animal):
    def nourrir(self):
        print("Nourrir le panda avec du bambou !")

class Lion(Animal):
    def nourrir(self):
        print("Nourrir le lion avec de la viande crue !")

class Zebre(Animal):
    def nourrir(self):
        print("Nourrir le zèbre avec du foin bien sec !")

po = Panda()
leo = Lion()
tok = Zebre()



zoo = [leo, po, tok]

for animal in zoo:
    animal.nourrir()