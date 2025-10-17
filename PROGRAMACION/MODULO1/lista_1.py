#definir una lista vacia y luego solicitar la carga de 5 numeros
#enteros por teclado y añadirlos a las listas

lista = [] # Lista vacia
print ("Cargar 5 numeros enteros")

num1 = int(input("ingrese el primer numero:  "))
lista.append(num1)

print (lista)
for x in range(4):
  x = int(input("ingrese los siguientes numeros: "))
  lista.append(x)
  print (lista) # muestra a medidda que se van agregando

print(lista) #esta fuera del bucle y muestra el arreglo completo