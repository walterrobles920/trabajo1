import math

#clase base
class Figura:
    def area(self):
        return 0  # o podrías devolver "Área no definida" o similar

#clase hija
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

def main():
    figuras = [
        Cuadrado(3),
        Cuadrado(5),
        Circulo(2),
        Circulo(4.5)
    ]

    for fig in figuras:
        nombre_clase = type(fig).__name__
        area = fig.area()
        print(f"Figura: {nombre_clase}, Área: {area:.2f}")

if __name__ == "__main__":
    main()

    