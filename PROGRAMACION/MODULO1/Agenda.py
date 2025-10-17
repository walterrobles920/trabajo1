# agenda_dni.py

import json
import os

AGENDA_FILE = "agenda_dni.json"

def cargar_agenda():
    if os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_agenda(agenda):
    with open(AGENDA_FILE, "w", encoding="utf-8") as f:
        json.dump(agenda, f, ensure_ascii=False, indent=2)

def pedir_datos():
    apellido = input("Apellido: ").strip()
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    while True:
        edad = input("Edad: ").strip()
        if edad.isdigit():
            edad = int(edad)
            break
        print("Edad inválida. Ingrese un número.")
    return {"apellido": apellido, "nombre": nombre, "telefono": telefono, "email": email, "edad": edad}

def main():
    agenda = cargar_agenda()
    while True:
        print("""
=== AGENDA POR DNI ===
1. Añadir o modificar contacto
2. Buscar contacto por DNI
3. Listar todos los contactos
4. Eliminar contacto por DNI
5. Salir
""")
        opcion = input("Seleccione opción (1‑5): ").strip()
        if opcion == "1":
            dni = input("Ingrese DNI: ").strip()
            if dni in agenda:
                print("Contacto existente:")
                print(json.dumps(agenda[dni], ensure_ascii=False, indent=2))
                resp = input("¿Desea modificarlo? (s/n): ").strip().lower()
                if resp == "s":
                    agenda[dni] = pedir_datos()
                    print("Contacto modificado.")
                else:
                    print("No se modificó.")
            else:
                print("DNI no encontrado. Ingrese datos del nuevo contacto:")
                agenda[dni] = pedir_datos()
                print("Contacto agregado.")
            guardar_agenda(agenda)

        elif opcion == "2":
            dni = input("DNI a buscar: ").strip()
            if dni in agenda:
                print("Datos del contacto:")
                print(json.dumps(agenda[dni], ensure_ascii=False, indent=2))
            else:
                print("No se encontró ningun contacto con ese DNI.")

        elif opcion == "3":
            if not agenda:
                print("Agenda vacía.")
            else:
                print(f"Total contactos: {len(agenda)}")
                for dni, datos in agenda.items():
                    print(f"DNI: {dni} — {datos['nombre']} {datos['apellido']}, Tel: {datos['telefono']}, Email: {datos['email']}, Edad: {datos['edad']}")

        elif opcion == "4":
            dni = input("DNI para eliminar: ").strip()
            if dni in agenda:
                del agenda[dni]
                guardar_agenda(agenda)
                print("Contacto eliminado.")
            else:
                print("No existe contacto con ese DNI.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
