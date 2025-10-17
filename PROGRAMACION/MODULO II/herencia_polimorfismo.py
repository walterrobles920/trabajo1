"""Herencia es la capacidad de heredar atributos y metodos de clase base (padre o superclase)
a una clase o hijo"""

#pólimorfismo: poli = muchas formas = muchas formas de hacer algo

class Animal: #clase padre. clase base, super clase
    def __init__(self, nombre):
        self.nombre = nombre        
    
    
class Perro (Animal): #clase hijo, clase derivada,subclase
    def ladrar (self):
        print(f"{self.nombre} dice guau!!!")

class Gato (Animal): #clase hijo, clase derivada,subclase
    def maullar (self):
        print(f"{self.nombre} dice miau!!!")

#instancia o creo el objeto
mi_perro = Perro ("firulais")
mi_perro.ladrar() #Firulais dice guau!
mi_gato = Gato("MICHI")
mi_gato.maullar()



