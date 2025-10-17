import os
os.system("cls")

class Auto:
    #metodo constructor con __init__ y inicializacion de atributos
     def __init__ (self, marca, modelo, color, anio, tipo):
      self.marca = marca
      self.modelo = modelo
      self.color = color
      self.anio = anio
      self.tipo = tipo

     def mostrar (self):
        print(f"marca: {self.marca}, modelo : {self.modelo}, color :{self.color}")



marca = input ("ingrese la marca del auto a crear")
modelo = input ("ingrese la modelo del auto")
color = input ("ingrese la color del auto")
anio = int(input ("ingrese el anio de fabricacion"))
tipo = input ("ingrese el tipo de automovil")

auto1 = Auto