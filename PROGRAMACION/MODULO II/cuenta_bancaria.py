class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = 0  # valor por defecto
        self.saldo = saldo_inicial  # usa el setter para validar

    # Getter: permite consultar el saldo
    @property
    def saldo(self):
        return self.__saldo

    # Setter: permite actualizar el saldo, validando que no sea negativo
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print("❌ Error: el saldo no puede ser negativo.")
        else:
            self.__saldo = nuevo_saldo

    # Método para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            print(f"✅ Se depositaron ${cantidad}. Saldo actual: ${self.saldo}")
        else:
            print("❌ No se puede depositar una cantidad negativa o cero.")

    # Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("❌ La cantidad a retirar debe ser mayor a cero.")
        elif cantidad > self.saldo:
            print("❌ Fondos insuficientes.")
        else:
            self.saldo = self.saldo - cantidad
            print(f"✅ Se retiraron ${cantidad}. Saldo actual: ${self.saldo}")

# Crear cuenta con $100 de saldo inicial
cuenta = CuentaBancaria(100)

cuenta.depositar(50)      # ✅ Se depositan 50 → Saldo: 150
cuenta.retirar(30)        # ✅ Se retiran 30 → Saldo: 120
cuenta.saldo = -500       # ❌ No se puede establecer saldo negativo
cuenta.retirar(200)       # ❌ Fondos insuficientes
print(f"Saldo final: ${cuenta.saldo}")
