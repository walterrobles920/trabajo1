#horario de materias= Tuplas de tuplas
horarío = (
    ("lunes", "matematicas"),
    ("martes","lengua"),
    ("miercoles","hitoria"),
    ("jueves","ingles"),
    ("viernes","geografia"))

print("horario semanal")
print(horarío)
for día , materia in horarío:
    print (f"{día} : {materia}")

#