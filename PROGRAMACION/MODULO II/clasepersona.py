import os
os.system ("cls")

class persona:
    def __init__(self, nombre, edad, DNI, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def mostar_datos (self):
        print(f"nombre: {self.nombre}, edad: {self.edad}, DNI: {self.DNI}")
        print(f"sexo: {self.sexo}, peso: {self.peso}, altura: {self.altura}")
        
persona1 = persona("walter",38, 32728251, "M", 86, 1.85)
persona1.mostar_datos()
