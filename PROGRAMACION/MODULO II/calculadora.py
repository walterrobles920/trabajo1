from abc import ABC, abstractmethod
import math
import os
os.system("cls") 

# Clase base abstracta
class Operacion(ABC):
    def __init__(self, numero1, numero2=None):
        self.set_numero1(numero1)
        self.set_numero2(numero2)

    def get_numero1(self):
        return self.__numero1

    def set_numero1(self, valor):
        if isinstance(valor, (int, float)):
            self.__numero1 = valor
        else:
            raise ValueError("El número 1 debe ser numérico")

    def get_numero2(self):
        return self.__numero2

    def set_numero2(self, valor):
        if valor is not None and not isinstance(valor, (int, float)):
            raise ValueError("El número 2 debe ser numérico o None")
        self.__numero2 = valor

    @abstractmethod
    def calcular(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Clases hijas
class Suma(Operacion):
    def calcular(self):
        return self.get_numero1() + self.get_numero2()

    def __str__(self):
        return f"{self.get_numero1()} + {self.get_numero2()} = {self.calcular()}"


class Resta(Operacion):
    def calcular(self):
        return self.get_numero1() - self.get_numero2()

    def __str__(self):
        return f"{self.get_numero1()} - {self.get_numero2()} = {self.calcular()}"


class Multiplicacion(Operacion):
    def calcular(self):
        return self.get_numero1() * self.get_numero2()

    def __str__(self):
        return f"{self.get_numero1()} * {self.get_numero2()} = {self.calcular()}"


class Division(Operacion):
    def calcular(self):
        if self.get_numero2() == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return self.get_numero1() / self.get_numero2()

    def __str__(self):
        return f"{self.get_numero1()} / {self.get_numero2()} = {self.calcular()}"


# Calculadora con historial
class Calculadora:
    def __init__(self):
        self.__historial = []

    def realizar_operacion(self, tipo, numero1, numero2=None):
        operaciones = {
            'suma': Suma,
            'resta': Resta,
            'multiplicacion': Multiplicacion,
            'division': Division,
        }

        if tipo not in operaciones:
            raise ValueError("Operación no válida")

        operacion = operaciones[tipo](numero1, numero2)
        resultado = operacion.calcular()
        self.__historial.append(operacion)
        return resultado

    def historial(self):
        return [str(op) for op in self.__historial]


# Calculadora Científica
class CalculadoraCientifica(Calculadora):
    def realizar_operacion(self, tipo, numero1, numero2=None):
        if tipo == 'potencia':
            resultado = math.pow(numero1, numero2)
            operacion_str = f"{numero1} ** {numero2} = {resultado}"
        elif tipo == 'raiz':
            if numero1 < 0:
                raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
            resultado = math.sqrt(numero1)
            operacion_str = f"√{numero1} = {resultado}"
        elif tipo == 'logaritmo':
            if numero1 <= 0:
                raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
            resultado = math.log10(numero1)
            operacion_str = f"log10({numero1}) = {resultado}"
        else:
            return super().realizar_operacion(tipo, numero1, numero2)

        self._Calculadora__historial.append(operacion_str)
        return resultado

    def historial(self):
        return [str(op) for op in self._Calculadora__historial]

"""def mostrar_menu():
    print("\n--- CALCULADORA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Logaritmo")
    print("8. Ver Historial")
    print("9. Salir")

def solicitar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def main():
    calc = CalculadoraCientifica()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                n1 = solicitar_numero("Número 1: ")
                n2 = solicitar_numero("Número 2: ")
                print("Resultado:", calc.realizar_operacion('suma', n1, n2))
            elif opcion == '2':
                n1 = solicitar_numero("Número 1: ")
                n2 = solicitar_numero("Número 2: ")
                print("Resultado:", calc.realizar_operacion('resta', n1, n2))
            elif opcion == '3':
                n1 = solicitar_numero("Número 1: ")
                n2 = solicitar_numero("Número 2: ")
                print("Resultado:", calc.realizar_operacion('multiplicacion', n1, n2))
            elif opcion == '4':
                n1 = solicitar_numero("Número 1: ")
                n2 = solicitar_numero("Número 2: ")
                print("Resultado:", calc.realizar_operacion('division', n1, n2))
            elif opcion == '5':
                n1 = solicitar_numero("Base: ")
                n2 = solicitar_numero("Exponente: ")
                print("Resultado:", calc.realizar_operacion('potencia', n1, n2))
            elif opcion == '6':
                n1 = solicitar_numero("Número: ")
                print("Resultado:", calc.realizar_operacion('raiz', n1))
            elif opcion == '7':
                n1 = solicitar_numero("Número: ")
                print("Resultado:", calc.realizar_operacion('logaritmo', n1))
            elif opcion == '8':
                print("\n--- HISTORIAL ---")
                for op in calc.historial():
                    print(op)
            elif opcion == '9':
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()"""
