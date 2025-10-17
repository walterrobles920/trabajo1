from abc import ABC, abstractmethod
import os
os.system("cls")

# Clase Abstracta y herencia
# Clase Corazón (Composición)

class Corazon:
    def __init__(self, frecuencia_cardiaca):
        self.__frecuencia_cardiaca = frecuencia_cardiaca
    def Latir (self):
        print(f"El corazon tiene una frecuencia cardiaca de:{self.get_frecuencia_cardiacafrecuencia_cardica}")    

    def get_frecuencia_cardiaca(self):
        return self.__frecuencia_cardiaca

    def set_frecuencia_cardiaca(self, frecuencia):
        self.__frecuencia_cardiaca = frecuencia

# Clase abstracta Mascota

class Mascota(ABC):
    def __init__(self, nombre, edad, corazon, dueño):
        self.__nombre = nombre
        self.__edad = edad
        self.__corazon = corazon  # Composición: sin corazón no vive
        self.__dueño = dueño  # Asociación: dueño es obligatorio
        dueño.agregar_mascota(self)

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_corazon(self):
        return self.__corazon

    def get_dueño(self):
        return self.__dueño

    @abstractmethod
    def calcular_costo_consulta(self):
        pass

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

    def comer(self):
        print(f"{self.__nombre} está comiendo.")


# Clase Perro (Herencia)

class Perro(Mascota):
    def __init__(self, nombre, edad, corazon, dueño, raza):
        super().__init__(nombre, edad, corazon, dueño)
        self.__raza = raza

    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Guau!")

    def calcular_costo_consulta(self):
        return 50.0  # Precio fijo para perros

    def mostrar_info(self):
        print(f"Perro - Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Raza: {self.__raza}, "
              f"Frecuencia Cardíaca: {self.get_corazon().get_frecuencia_cardiaca()}, "
              f"Dueño: {self.get_dueño().get_nombre()}")

# Clase Gato (Herencia)

class Gato(Mascota):
    def __init__(self, nombre, edad, corazon, dueño, color_pelo):
        super().__init__(nombre, edad, corazon, dueño)
        self.__color_pelo = color_pelo

    def hacer_sonido(self):
        print(f"{self.get_nombre()} dice: ¡Miau!")

    def calcular_costo_consulta(self):
        return 40.0  # Precio fijo para gatos

    def mostrar_info(self):
        print(f"Gato - Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Color de Pelo: {self.__color_pelo}, "
              f"Frecuencia Cardíaca: {self.get_corazon().get_frecuencia_cardiaca()}, "
              f"Dueño: {self.get_dueño().get_nombre()}")

# Clase Dueño (Asociación)

class Dueno:
    def __init__(self, nombre, telefono):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__mascotas = []  # Uno a muchos

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def listar_mascotas(self):
        for mascota in self.__mascotas:
            mascota.mostrar_info()

# Clase Veterinaria (Agregación)

class Veterinaria:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mascotas = []  # Agregación débil

    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def listar_mascotas(self):
        print(f"Mascotas atendidas en {self.__nombre}:")
        for mascota in self.__mascotas:
            mascota.mostrar_info()

# Ejemplo de uso

if __name__ == "__main__":
    # Crear dueño
    dueño = []
    dueno = input("ingrese el nombre del dueño: ")

    # Crear corazones
    corazon_perro = input("ingrese la frecuencia cardiaca del perro:")
    corazon_gato = input("ingrese la frecuencia cardiaca del gato:")

    # Crear mascotas
    mascotas = []
    perro_n = input("ingrese el nombre del perro: ")
    gato_n = input ("ingrese el nombre del gato: " )

    perro_fc = input("ingrese la frecuencia cardiaca de perro: ")
    gato_fc = input ("ingrese la frecuencia cardiaca de gato: " )
    
    perro_edad = input("ingrese la edad del perro: ")
    gato_edad = input("ingrese la edad del gato: ")

    perro_raza = input("ingrese la raza del perro es: ")
    gato_raza = input ("ingrese la raza del gato es: ")
#perro_fc = input("ingrese la frecuencia cardiaca de perro es:{corazon_perro}")

    # Crear veterinaria 
    vet = Veterinaria("VetLife")   
    vet.agregar_mascota(Perro)
    vet.agregar_mascota(Gato) 

    # Mostrar información
    vet.listar_mascotas()


    # Sonidos
    Perro.hacer_sonido()
    Gato.hacer_sonido()
 
    # Costos
    print(f"Costo consulta de {Perro.get_nombre()}: ${Perro.calcular_costo_consulta()}")
    print(f"Costo consulta de {Gato.get_nombre()}: ${Gato.calcular_costo_consulta()}")
