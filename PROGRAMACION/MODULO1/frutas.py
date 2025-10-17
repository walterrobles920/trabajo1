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
print = ("¿necesita algo mas?")
 
while True:
     if frutas == "salir":
        print ("Gracias por su compra")
        break
     
     if frutas in precios_frutas:
        total = precios_frutas[frutas]*kilos
        print(f"El precio por kilo es {kilos} de la {frutas} y es ${total}")
     else:
        print(f"no tenemos esa {frutas}")    
