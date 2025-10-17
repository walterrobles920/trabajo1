from abc import ABC, abstractmethod
import os
os.system("cls")

# Definimos la clase abstracta Empleado
class Empleado(ABC):
    def __init__(self, nombre, dni, salario_base):
        self._nombre = nombre #._ me define encapsulamiento quiere decir protege esos datos
        self._dni = dni
        self._salario_base = salario_base #inicializa mi constructor de clase son atributos globales que heredan las clases hijas

    @abstractmethod
    def calcular_salario(self):
        pass

    def mostrar_info(self):
        print(f"\nNombre: {self._nombre}")
        print(f"DNI: {self._dni}")
        print(f"Salario: {self.calcular_salario()}")

# Clases hijas de Empleado
class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, dni, salario_base):
        super().__init__(nombre, dni, salario_base)

    def calcular_salario(self):
        return self._salario_base + (self._salario_base * 0.1)

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, dni, salario_base, horas):
        super().__init__(nombre, dni, salario_base)
        self._horas = horas

    def calcular_salario(self):
        return self._salario_base * self._horas

def imprimir_detalles(empleado):#
    empleado.mostrar_info() #invoco un metodo 

# Instanciando empleados
empleado1 = EmpleadoAsalariado("Juan Garcia", "34885946", 750000)
empleado2 = EmpleadoPorHoras("Ana Rivero", "32548977", 6000, 160)

imprimir_detalles(empleado1)
imprimir_detalles(empleado2)