from abc import ABC, abstractmethod
import os
os.system ("cls")

class Cuenta(ABC):
    @abstractmethod #decorador
    def depositar (self, monto):
        pass
    @abstractmethod
    def retirar (self,monto):
        pass
#encapsulamiento
#clase hijo

class cuentabancaria(Cuenta):
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, monto):
        self._saldo

    def retirar(self, monto):
    if monto >0 and monto <= monto
        self._saldo -= monto
        print(f"Retiro exitoso. Saldo Actual:{self._saldo}") 
    else:
        print("Fondos Insuficienres o monto invalido")
    
def versaldo (self)