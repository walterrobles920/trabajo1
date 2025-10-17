
###polimorfismo
class Animal: #clase padre
    def __init__(self, nombre):
     self.nombre = nombre
    def sonido (self):
       pass

class Perro (Animal):
    def sonido(self):
        return "guau"
        
class Gato (Animal):
    def sonido(self):
        return f"{self.nombre} dice miau"
    
class Vaca (Animal):
    def sonido(self):
        return f"{self.nombre} dice Muuu"   
    
#instancia o creo el objeto
# lista de objetos
animales = [Perro("bovi"), Gato("Michifuz"), Vaca("Lola")]

#recorrer lista para mostrar los mensajes
for animal in animales:
    mi_perro = Perro("Firulai")
    print (mi_perro.sonido())
    mi_gato = Gato("Michi")
    print (mi_gato.sonido())
    mi_vaca = Vaca("Lola")
    print (mi_vaca.sonido())
