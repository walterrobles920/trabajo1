#horario de materias= Tuplas de tuplas
horarío = (
    ("lunes", "matematicas"),
    ("martes","lengua"),
    ("miercoles","hitoria"),
    ("jueves","ingles"),
    ("viernes","geografia"))

print("horario semanal")
print(horarío)
for día , materia in horarío:
    print (f"{día} : {materia}")

# 2.lista - lista de compras
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
      monto = float( imput (f"ingrese el monto de gastos por {cat}: $"))
      fila.append(monto)
gasto.append(fila)

#gastos por semana

print ("\nGastos semanas:")
for i, semana in range(4):
   total_semana= sum(semana)
   print(f"semana {i+1}: $ {total_semana:.2f}")



