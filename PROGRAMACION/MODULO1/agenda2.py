agenda = {}
def agregar_modificar(dni):
    if dni in agenda:
        print(f"dni encontrado : {dni} = {agenda}")
        opcion = input("deseas modificar los datos ? (s/n)").lower()
        if opcion != "s" :
            return
        
    dni = input ("ingrese el DNI de usuario: ")
    nombre = input ("ingrese el nombre de usuario: ")
    apellido = input (" ingrese el apellido del usuario: ")
    telefono = input ("ingrese el telefono del usuario: ")
    email = input ("email :")
    edad = input ("ingrese la edad del usuario: ")

datos_personales = {"nombre": nombre,
                    "apellido": apellido.
                    "telefono": telefono,
                    "email": email,
                    "edad" : edad }
agenda[dni] = datos datos_personales
print ("contacto guardado modificado correctamente")
print (agenda)

def buscar_nombre (cadena):
    cadena =cadena.lower()
    print (f"buscando los contactos que comiencen con {cadena} :")
    for dni, datos_personales in agenda.items():
        nombre = datos_personales["nombre"].lower()
        if nombre.startswith(cadena)
        print (f"los datos son")