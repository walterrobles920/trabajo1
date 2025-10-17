import platform
import os
os.system("cls")

# Padrón electoral (documentos válidos)
padron_electoral = [
    "1001", "1002", "1003", "1004", "1005", "1006", "1007"
]

# Documento para terminar la votación
DOCUMENTO_SALIDA = "terminar"

# Partidos disponibles
partidos = {
    "1": "Partido Azul",
    "2": "Partido Verde"
}

# Resultados de los votos
resultados = []

# Limpiar consola
def limpiar_consola():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Documentos que ya votaron
ya_votaron = []

def mostrar_menu():
    print("\n=== Elecciones Centro de Estudiantes 2025 ===")
    print("1 - Partido Azul")
    print("2 - Partido Verde")

def votar():
    doc = input("\nIngrese su número de documento: ")

    if doc == DOCUMENTO_SALIDA:
        return False  # Señal para salir del bucle

    if doc not in padron_electoral:
        print("❌ Este documento NO está habilitado para votar.")
        return True

    if doc in ya_votaron:
        print("❌ Este documento YA ha votado.")
        return True

    mostrar_menu()
    opcion = input("Seleccione el número del partido por el que desea votar: ")

    if opcion in partidos:
        partido_elegido = partidos[opcion]
        resultados.append((doc, partido_elegido))
        ya_votaron.append(doc)
        print(" ✅ Gracias por votar")
    else:
        print("❌ Opción no válida. Voto no registrado.")

    return True

# Bucle de votación
while True:
    continuar = votar()
    if not continuar:
        break

# Mostrar resultados
print("\n=== Resultados Finales ===")

# Contar votos
conteo = {
    "Partido Azul": 0,
    "Partido Verde": 0
}

for doc, partido in resultados:
    if partido in conteo:
        conteo[partido] += 1

# Mostrar conteo de votos
print("\n📊 Conteo de votos:")
for partido, votos in conteo.items():
    print(f"{partido}: {votos} votos")

# Determinar ganador
if conteo["Partido Azul"] > conteo["Partido Verde"]:
    print("\n🎉 ¡Ganador: Partido Azul!")
elif conteo["Partido Verde"] > conteo["Partido Azul"]:
    print("\n🎉 ¡Ganador: Partido Verde!")
else:
    print("\n⚖️ Empate entre ambos partidos.")
