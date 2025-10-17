# Programa de Herencia - Sistema de Clasificación Animal
# Clase base Animal con clases hijas: Herbívoro, Carnívoro, Omnívoro

class Animal:
    """
    Clase base Animal que contiene los atributos y métodos comunes
    para todos los tipos de animales
    """
    def __init__(self, nombre, edad, peso, habitat):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.habitat = habitat
    
    def mostrar_info_basica(self):
        """Método para mostrar información básica del animal"""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Hábitat: {self.habitat}")
    
    def hacer_sonido(self):
        """Método genérico para hacer sonido"""
        print(f"{self.nombre} hace un sonido")


class Herbivoro(Animal):
    """
    Clase hija Herbívoro que hereda de Animal
    Atributos adicionales específicos para herbívoros
    """
    def __init__(self, nombre, edad, peso, habitat, tipo_planta_favorita, horas_pastoreo):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, peso, habitat)
        # Atributos específicos de herbívoros
        self.tipo_planta_favorita = tipo_planta_favorita
        self.horas_pastoreo = horas_pastoreo
        self.tipo_alimentacion = "Herbívoro"
    
    def mostrar_info_completa(self):
        """Mostrar toda la información del herbívoro"""
        print("=== INFORMACIÓN DEL HERBÍVORO ===")
        self.mostrar_info_basica()
        print(f"Tipo de alimentación: {self.tipo_alimentacion}")
        print(f"Planta favorita: {self.tipo_planta_favorita}")
        print(f"Horas de pastoreo diarias: {self.horas_pastoreo}")
    
    def pastar(self):
        """Método específico de herbívoros"""
        print(f"{self.nombre} está pastando {self.tipo_planta_favorita}")


class Carnivoro(Animal):
    """
    Clase hija Carnívoro que hereda de Animal
    Atributos adicionales específicos para carnívoros
    """
    def __init__(self, nombre, edad, peso, habitat, tipo_presa_favorita, velocidad_caza):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, peso, habitat)
        # Atributos específicos de carnívoros
        self.tipo_presa_favorita = tipo_presa_favorita
        self.velocidad_caza = velocidad_caza
        self.tipo_alimentacion = "Carnívoro"
    
    def mostrar_info_completa(self):
        """Mostrar toda la información del carnívoro"""
        print("=== INFORMACIÓN DEL CARNÍVORO ===")
        self.mostrar_info_basica()
        print(f"Tipo de alimentación: {self.tipo_alimentacion}")
        print(f"Presa favorita: {self.tipo_presa_favorita}")
        print(f"Velocidad de caza: {self.velocidad_caza} km/h")
    
    def cazar(self):
        """Método específico de carnívoros"""
        print(f"{self.nombre} está cazando {self.tipo_presa_favorita} a {self.velocidad_caza} km/h")


class Omnivoro(Animal):
    """
    Clase hija Omnívoro que hereda de Animal
    Atributos adicionales específicos para omnívoros
    """
    def __init__(self, nombre, edad, peso, habitat, alimento_vegetal_favorito, alimento_animal_favorito, porcentaje_vegetales):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, peso, habitat)
        # Atributos específicos de omnívoros
        self.alimento_vegetal_favorito = alimento_vegetal_favorito
        self.alimento_animal_favorito = alimento_animal_favorito
        self.porcentaje_vegetales = porcentaje_vegetales
        self.tipo_alimentacion = "Omnívoro"
    
    def mostrar_info_completa(self):
        """Mostrar toda la información del omnívoro"""
        print("=== INFORMACIÓN DEL OMNÍVORO ===")
        self.mostrar_info_basica()
        print(f"Tipo de alimentación: {self.tipo_alimentacion}")
        print(f"Alimento vegetal favorito: {self.alimento_vegetal_favorito}")
        print(f"Alimento animal favorito: {self.alimento_animal_favorito}")
        print(f"Porcentaje de vegetales en dieta: {self.porcentaje_vegetales}%")
    
    def alimentarse_variado(self):
        """Método específico de omnívoros"""
        print(f"{self.nombre} se alimenta tanto de {self.alimento_vegetal_favorito} como de {self.alimento_animal_favorito}")


# ================== PROGRAMA PRINCIPAL ==================

def main():
    print("🐾 SISTEMA DE CLASIFICACIÓN ANIMAL - HERENCIA 🐾")
    print("=" * 55)
    
    # Instanciar objetos de cada tipo
    
    # 1. Crear un objeto Herbívoro
    herbivoro1 = Herbivoro(
        nombre="Cebra",
        edad=5,
        peso=300,
        habitat="Sabana africana",
        tipo_planta_favorita="Pasto tierno",
        horas_pastoreo=12
    )
    
    # 2. Crear un objeto Carnívoro
    carnivoro1 = Carnivoro(
        nombre="León",
        edad=8,
        peso=180,
        habitat="Sabana africana",
        tipo_presa_favorita="Ñu",
        velocidad_caza=60
    )
    
    # 3. Crear un objeto Omnívoro
    omnivoro1 = Omnivoro(
        nombre="Oso Pardo",
        edad=12,
        peso=400,
        habitat="Bosque templado",
        alimento_vegetal_favorito="Bayas y miel",
        alimento_animal_favorito="Salmón",
        porcentaje_vegetales=70
    )
    
    # Mostrar información de todos los objetos
    print("\n" + "=" * 55)
    herbivoro1.mostrar_info_completa()
    herbivoro1.pastar()
    
    print("\n" + "=" * 55)
    carnivoro1.mostrar_info_completa()
    carnivoro1.cazar()
    
    print("\n" + "=" * 55)
    omnivoro1.mostrar_info_completa()
    omnivoro1.alimentarse_variado()
    
    # Demostrar el polimorfismo - todos pueden hacer sonido
    print("\n" + "=" * 55)
    print("🔊 DEMOSTRACIÓN DE POLIMORFISMO - SONIDOS:")
    print("-" * 55)
    herbivoro1.hacer_sonido()
    carnivoro1.hacer_sonido()
    omnivoro1.hacer_sonido()
    
    # Crear más ejemplos
    print("\n" + "=" * 55)
    print("📋 EJEMPLOS ADICIONALES:")
    print("-" * 55)
    
    # Más herbívoros
    elefante = Herbivoro("Elefante", 25, 5000, "Sabana", "Hojas de acacia", 16)
    elefante.mostrar_info_completa()
    
    print("\n" + "-" * 55)
    
    # Más carnívoros
    tiburon = Carnivoro("Tiburón Blanco", 15, 2000, "Océano", "Focas", 40)
    tiburon.mostrar_info_completa()
    
    print("\n" + "-" * 55)
    
    # Más omnívoros
    cerdo = Omnivoro("Cerdo Doméstico", 3, 150, "Granja", "Vegetales", "Insectos", 60)
    cerdo.mostrar_info_completa()
    
    print("\n" + "=" * 55)
    print("✅ PROGRAMA COMPLETADO EXITOSAMENTE")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()