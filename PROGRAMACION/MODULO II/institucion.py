from abc import ABC, abstractmethod
import os
os.system("cls")

        
class Persona:
    def __init__(self, nombre, identificacion, email):
        self.nombre = nombre
        self._identificacion = identificacion  # dato sensible
        self._email = email  # dato sensible

    def realizar_accion(self):
        raise NotImplementedError("Debe implementarse en las subclases")

    def obtener_email(self):
        return self._email

    def modificar_email(self, nuevo_email):
        # Solo si cumple ciertas condiciones
        self._email = nuevo_email
       
class Estudiante(Persona):
    def __init__(self, nombre, identificacion, email, matricula):
        super().__init__(nombre, identificacion, email)
        self.matricula = matricula
        self.cursos_inscritos = []

    def realizar_accion(self):
        print(f"{self.nombre} está asistiendo a clase.")

class Trabajador(Persona):
    def __init__(self, nombre, identificacion, email, puesto):
        super().__init__(nombre, identificacion, email)
        self.puesto = puesto
        self.actividades_coordinadas = []

    def realizar_accion(self):
        print(f"{self.nombre} está coordinando una actividad.")

class Actividad:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # curso o taller
        self.participantes = []
        self.coordinador = None
        self.recursos = []

    def agregar_participante(self, persona):
        self.participantes.append(persona)

    def asignar_coordinador(self, trabajador):
        self.coordinador = trabajador
        trabajador.actividades_coordinadas.append(self)

    def agregar_recurso(self, recurso):
        self.recursos.append(recurso)

class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre

class RecursoTemporal(Recurso):
    def __init__(self, nombre):
        super().__init__(nombre)

class RecursoPermanente(Recurso):
    def __init__(self, nombre):
        super().__init__(nombre)

# Crear personas
est1 = Estudiante("Ana", "123", "ana@email.com", "MAT-001")
trab1 = Trabajador("Prof. Luis", "456", "luis@email.com", "Docente")

# Crear actividad
curso_python = Actividad("Curso de Python", "curso")
curso_python.asignar_coordinador(trab1)
curso_python.agregar_participante(est1)

# Recursos
libro = RecursoPermanente("Libro de Python")
pc = RecursoTemporal("Laptop prestada")

curso_python.agregar_recurso(libro)
curso_python.agregar_recurso(pc)

# Acciones
est1.realizar_accion()
trab1.realizar_accion()
