import os
os.system("cls")
class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        
    def __str__(self):
        if self.puntaje >= 1000:
            nivel = "Experto"
        else:
            nivel = "Principiante"

        return(f"nivel {nivel} persona: {self.nombre} puntaje: {self.puntaje}")

  #Principal

jugador1 = Jugador ("Maria", 800)    
jugador2 = Jugador ("Pedro", 2500)      

print (jugador1)
print (jugador2)
