"""Escribe un programa que guarde en un diccionario los precios de
las frutas de la tabla, pregunte al usuario por una fruta, un numero de kilos 
y muestre por pantalla el precio de ese numero de kilos de fruta.
si la fruta no esta en el diccionario debe mostrar un mensaje informando de ello"""

precios_frutas = {
    "manzana": 1500,
    "pera" : 2000,
    "naranja" : 1300,
    "uva": 3400,
    "banana" : 1200,
    "mandarina" : 1800,
}
frutas = input("¿Que fruta busca?: ").lower()
kilos = float(input("¿Cuantos kilos necesita?: "))
 
if frutas in precios_frutas:
    total = precios_frutas[frutas]*kilos
    print(f"El precio por kilo es {kilos} de la {frutas} y es ${total}")
else:
     print(f"no tenemos esa (frutas)")    
