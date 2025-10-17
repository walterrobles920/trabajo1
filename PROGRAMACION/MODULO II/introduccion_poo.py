#crear clase animal
class Animal:
    def __init__(self,nombre, especie, edad):
        self.nombre = nombre #atributo guarda el nombre del animal
        self.especie = especie #atributo guarda especie
        self.edad = edad

    def hablar(self):
        if self.especie == "felino":
            print(f"Es una anmal de especie{self.especie}o conocido como gato")
            print(f"{self.nombre}dice:Miau")
        elif self.especie == "canino":
            print(f"Es una anmal de especie{self.especie}o conocido como perro")
            print(f"{self.nombre}dice:Guau")
        elif self.especie == "Ave":
            print(f"Es una anmal de especie{self.especie}o conocido como pato")
            print(f"{self.nombre}dice:Cua Cua") 
        elif self.especie == "bovino":
            print(f"Es una anmal de especie{self.especie}o conocido como vaca")
            print(f"{self.nombre}dice:Muuuuuu")   
        else:
            print (f"{self.nombre} sonido desconocido")

    def edad (self):
        print(f"la edad{self.nombre} es: {self.edad}")     
#crear los objetos a partir de esas clase eso seria la intanciacion de clase
#programa principal           