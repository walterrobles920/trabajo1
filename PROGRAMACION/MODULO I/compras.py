#lista - lista de compras
print ("\nLista de compras")
compras = []

# cargar productos de la lista
cantidad = int(input("¿cuantos productos queres comprar?"))
for i in range (cantidad):
    producto = input ( " ingresar producto: ")
    compras.append(producto)

# mostrar lista
print ("\nProducto en la lista")
for producto in compras:
  print(f" * {producto}")

# 3.Matriz
print ("\nRegistro de gastos semanales:")
categorias = ["comida", "transporte", "Entretenimiento"]
gasto = []
for semana in range (4):
   fila = []
   for cat in categorias:
      monto = float( input (f"ingrese el monto de gastos por {cat}: $"))
      fila.append(monto)
gasto.append(fila)
print (gasto)

#gastos por semana

print ("\nGastos semanas:")
for i, semana in enumerate(gasto):
   total_semana= sum(semana)
   print(f"semana {i+1}: $ {total_semana:.2f}")



def cargar_matriz (fila, columna):
    matriz = []
    print ("\nIngrese los valores de la matriz:")
    for i in range (fila):
        fila = []
        for j in range (columna):
            valor = int (input (f"Ingrese el valor en posición [{i}] [{j}]:    "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def  mostrar_matriz (matriz):
    print ("\nMatriz Cargada")
    for fila in matriz:
        print ("\t" .join(str(x) for  x in fila ))

def suma_filas (matriz):
    print ("\n Suma de Filas")
    for i, fila in enumerate (matriz):
        suma = sum (fila)
        print (f"fila {i+1} = {suma}")
    #return [sum(fila) for fila in matriz]


def suma_columnas (matriz):
    print ("\n Suma de Columnas")
    columna = len (matriz [0])
    for j in range (columna):
        suma = sum (matriz [i][j] for i in range (len(matriz)))
        print (f"Columna {j+1} = {suma}")
    #return [sum (matriz [fila][columna] for fila  in range (len(matriz))) for columna in

def suma_total(matriz):
    total = sum (sum (fila) for fila in matriz)
    print (f" Suma total es: {total}")
   

# Programa principal
fila = int(input("Ingrese la cantidad de filas que necesita su matriz:   "))
columna = int(input("Ingrese la cantidad de columnas que necesita su matriz:   "))

matriz = cargar_matriz(fila, columna)
print (matriz)
mostrar_matriz (matriz)
suma_filas(matriz)
suma_columnas(matriz)
suma_total(matriz)