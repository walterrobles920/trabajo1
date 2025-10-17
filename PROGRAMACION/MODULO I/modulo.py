import modulo1
import os
import time

valor1 = float(input("ingrese el primer valor: "))

valor2 = float(input("ingrese el segundo valor: "))

time.sleep(2)

resultado = modulo1.f_sumar(valor1, valor2)

print(f"la suma de los valores ingresados es: {resultado}")

time.sleep(2)

os.system("cls")