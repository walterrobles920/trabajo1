#deque
from collections import deque

pila = deque()
pila.append(1)
pila.append(2)
pila.append(3)
print("pila",pila)

sacar_elemento = pila.pop()
print("el elemento sacado de la pila es ", sacar_elemento)
print("pila despues de pop", pila)

#Cola(queue)FIFO

cola = deque()#COLA VACIA
cola.append(1)
cola.append(2)
cola.append(3)

print("cola", cola)
quitar_elemento = cola.popleft()#ubicacion de elemento a sacar

print("cola despues del pop: ", cola)

#Pila(stack) LIFO

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print("pila",pila)

sacar_elemento = pila.pop()
print("el elemento sacado de la pila es ", sacar_elemento)
print("pila despues de pop", pila)


#Cola(stack)FIFO

cola = []
cola.append(1)
cola.append(2)
cola.append(3)

print("cola", cola)
quitar_elemento = cola.pop(0)#ubicacion de elemento a sacar

print("cola despues del pop: ", cola)
#libreria deque

# Atencion al cliente
cola_clientes = deque(["Juan","Pedro", "Maria", "Jose"])

while cola_clientes:
    cliente = cola_clientes.popleft()
    print (f"Atendiendo al cliente: ",{cliente})