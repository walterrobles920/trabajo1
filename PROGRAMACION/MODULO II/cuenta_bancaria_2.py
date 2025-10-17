from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, pin, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__pin = pin
        self.__saldo = 0
        self.saldo = saldo_inicial
        self.movimientos = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print("❌ Saldo no puede ser negativo.")
        else:
            self.__saldo = nuevo_saldo

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

    def registrar_movimiento(self, tipo, cantidad):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.movimientos.append((fecha, tipo, cantidad))

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            self.registrar_movimiento("Depósito", cantidad)
            print(f"✅ Se depositaron ${cantidad}.")
        else:
            print("❌ Cantidad inválida.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("❌ Monto inválido.")
        elif cantidad > self.saldo:
            print("❌ Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            self.registrar_movimiento("Retiro", cantidad)
            print(f"✅ Se retiraron ${cantidad}.")

    def mostrar_info(self):
        print(f"\n💳 Cuenta: {self.numero_cuenta}")
        print(f"👤 Titular: {self.titular}")
        print(f"💰 Saldo: ${self.saldo}")

    def mostrar_movimientos(self):
        if not self.movimientos:
            print("📭 Sin movimientos.")
        else:
            print("\n📜 Movimientos:")
            for fecha, tipo, cantidad in self.movimientos:
                print(f"{fecha} - {tipo}: ${cantidad}")

    def generar_extracto_txt(self):
        archivo = f"extracto_{self.numero_cuenta}.txt"
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(f"Extracto - Cuenta {self.numero_cuenta}\n")
            f.write(f"Titular: {self.titular}\nSaldo: ${self.saldo}\n\n")
            f.write("Movimientos:\n")
            for fecha, tipo, cantidad in self.movimientos:
                f.write(f"{fecha} - {tipo}: ${cantidad}\n")
        print(f"📁 Extracto guardado en {archivo}")

    def generar_extracto_pdf(self):
        archivo = f"extracto_{self.numero_cuenta}.pdf"
        c = canvas.Canvas(archivo, pagesize=A4)
        ancho, alto = A4
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, alto - 50, "Extracto de Cuenta")
        c.setFont("Helvetica", 12)
        c.drawString(50, alto - 90, f"Titular: {self.titular}")
        c.drawString(50, alto - 110, f"Número: {self.numero_cuenta}")
        c.drawString(50, alto - 130, f"Saldo actual: ${self.saldo}")
        c.drawString(50, alto - 170, "Movimientos:")

        y = alto - 190
        for fecha, tipo, cantidad in self.movimientos:
            c.drawString(60, y, f"{fecha} - {tipo}: ${cantidad}")
            y -= 20
            if y < 50:
                c.showPage()
                y = alto - 50
        c.save()
        print(f"📄 PDF guardado en {archivo}")
# Diccionario de cuentas
banco = {}

def crear_cuenta():
    print("\n--- Crear nueva cuenta ---")
    numero = input("Número de cuenta: ")
    if numero in banco:
        print("❌ La cuenta ya existe.")
        return
    nombre = input("Titular: ")
    pin = input("PIN (4 dígitos): ")
    try:
        saldo = float(input("Saldo inicial: "))
    except:
        saldo = 0
    banco[numero] = CuentaBancaria(numero, nombre, pin, saldo)
    print("✅ Cuenta creada con éxito.")

def acceder_cuenta():
    print("\n--- Iniciar sesión ---")
    numero = input("Número de cuenta: ")
    pin = input("PIN: ")
    cuenta = banco.get(numero)
    if not cuenta or not cuenta.validar_pin(pin):
        print("❌ Datos incorrectos.")
        return

    while True:
        print(f"\n--- Menú Cuenta {numero} ---")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver movimientos")
        print("5. Generar extracto TXT")
        print("6. Generar extracto PDF")
        print("7. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cuenta.mostrar_info()
        elif opcion == "2":
            monto = float(input("Monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "3":
            monto = float(input("Monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "4":
            cuenta.mostrar_movimientos()
        elif opcion == "5":
            cuenta.generar_extracto_txt()
        elif opcion == "6":
            cuenta.generar_extracto_pdf()
        elif opcion == "7":
            print("👋 Sesión cerrada.")
            break
        else:
            print("❌ Opción inválida.")

# Bucle del sistema
while True:
    print("\n=== Banco Virtual ===")
    print("1. Crear cuenta")
    print("2. Acceder a cuenta")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        acceder_cuenta()
    elif opcion == "3":
        print("👋 Hasta luego.")
        break
    else:
        print("❌ Opción inválida.")
