"""Almacenar una lista de sueldos (valores float) de 6 operarios
imprimir la lista y calcular el sueldo promedio"""

sueldo = []
print ("ingresar 6 sueldos")
s1 = float(input("Ingresar el primer sueldo: ")) 
sueldo.append(s1)
suma = s1

for x in range (5):
    x = int(input("Ingresar los siguientes sueldos: "))
    sueldo.append(x)
    suma = suma + x

print ("Lista de sueldos: ", sueldo)
prom = suma/6
print ("promedio de sueldos: ", prom)