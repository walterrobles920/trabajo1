"""Vamoa a crear un programna donde vamos a declarar un diccionario para guardar
los precios de las distimtas frutas. el programa pedira el nombre de la fruta y 
la cantidad que se a vendido y nos mostrara el precio final de la fruta a partir
de los datos guardados en el diccionario. Si la fruta no existe nos dara error. 
tras cada consulta del programa nos preguntara si queremos hacer otra consulta"""

precios_frutas = {
    "manzana": 1.500,
    "banana": 1.100,
    "naranja": 1.000,
    "frutilla": 3.000,
    "uva": 2.000,
    "pera" : 1.200 }

def consultar_precio():
    while True:
        fruta = input("Introduce el nombre de la fruta: ")
        
        if fruta in precios_frutas:
            try:
                cantidad = float(input(f"Introduce la cantidad de {fruta} vendida: "))
                if cantidad < 0:
                    raise ValueError("La cantidad no existe.")
                
                precio_total = precios_frutas[fruta] * cantidad
                print(f"El precio total de {cantidad} {fruta}(s) es: ${precio_total:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: La fruta no existe.")
        
        otra_consulta = input("¿Quieres hacer otra consulta? (sí/no): ")
        if otra_consulta != 'sí':
            print ("Introduce el nombre de la fruta: ")
        elif otra_consulta == 'no':
            print("¡Gracias por usar el programa!")
        break

consultar_precio()