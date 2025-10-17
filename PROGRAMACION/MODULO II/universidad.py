from abc import ABC, abstractmethod
from datetime import date
import os
os.system("cls")

# Clase abstracta base
class Persona(ABC):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
   
    @abstractmethod
    def obtener_rol(self):
        pass
   
    def mostrar_info(self):
        print(f"Nombre: {self._nombre} {self._apellido}")
        print(f"DNI: {self._dni}")
        print(f"Fecha de nacimiento: {self._fecha_nacimiento}")
        print(f"Rol: {self.obtener_rol()}")

# Clases subclase - Herencia
class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, numero_matricula, carrera, año_ingreso):
        super().__init__(nombre, apellido, dni, fecha_nacimiento)
        self._numero_matricula = numero_matricula
        self._carrera = carrera
        self._año_ingreso = año_ingreso
        self._cursos_inscritos = []
   
    def obtener_rol(self):
        return f"Estudiante de {self._carrera}"
   
    def inscribir_curso(self, curso):
        if curso not in self._cursos_inscritos:
            self._cursos_inscritos.append(curso)
            curso.inscribir_estudiante(self)

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, codigo_empleado, departamento, años_experiencia):
        super().__init__(nombre, apellido, dni, fecha_nacimiento)
        self._codigo_empleado = codigo_empleado
        self._departamento = departamento
        self._años_experiencia = años_experiencia
        self._cursos_dictados = []
   
    def obtener_rol(self):
        return f"Profesor del Departamento de {self._departamento}"
   
    def dictar_curso(self, curso):
        if curso not in self._cursos_dictados:
            self._cursos_dictados.append(curso)
            curso.asignar_profesor(self)

class Administrativo(Persona):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, codigo_empleado, area, cargo):
        super().__init__(nombre, apellido, dni, fecha_nacimiento)
        self._codigo_empleado = codigo_empleado
        self._area = area
        self._cargo = cargo
   
    def obtener_rol(self):
        return f"Personal Administrativo - {self._cargo}"

# Otras clases del sistema
class Curso:
    def __init__(self, codigo, nombre, creditos, horario):
        self._codigo = codigo
        self._nombre = nombre
        self._creditos = creditos
        self._horario = horario
        self._estudiantes_inscritos = []
        self._profesor = None
   
    def inscribir_estudiante(self, estudiante):
        if estudiante not in self._estudiantes_inscritos:
            self._estudiantes_inscritos.append(estudiante)
   
    def asignar_profesor(self, profesor):
        self._profesor = profesor
   
    def mostrar_info(self):
        print(f"\n--- CURSO ---")
        print(f"Código: {self._codigo}")
        print(f"Nombre: {self._nombre}")
        print(f"Créditos: {self._creditos}")
        print(f"Horario: {self._horario}")
        if self._profesor:
            print(f"Profesor: {self._profesor._nombre} {self._profesor._apellido}")
        print(f"Estudiantes inscritos: {len(self._estudiantes_inscritos)}")

class Departamento:
    def __init__(self, nombre, codigo, ubicacion):
        self._nombre = nombre
        self._codigo = codigo
        self._ubicacion = ubicacion
        self._profesores = []  # Agregación
   
    def agregar_profesor(self, profesor):
        if profesor not in self._profesores:
            self._profesores.append(profesor)
   
    def mostrar_info(self):
        print(f"\n--- DEPARTAMENTO ---")
        print(f"Nombre: {self._nombre}")
        print(f"Código: {self._codigo}")
        print(f"Ubicación: {self._ubicacion}")
        print(f"Profesores: {len(self._profesores)}")

class Universidad:
    def __init__(self, nombre, direccion, año_fundacion):
        self._nombre = nombre
        self._direccion = direccion
        self._año_fundacion = año_fundacion
        self._departamentos = []  # Composición
   
    def agregar_departamento(self, departamento):
        self._departamentos.append(departamento)
   
    def mostrar_info(self):
        print(f"\n=== UNIVERSIDAD ===")
        print(f"Nombre: {self._nombre}")
        print(f"Dirección: {self._direccion}")
        print(f"Año de fundación: {self._año_fundacion}")
        print(f"Departamentos: {len(self._departamentos)}")

# Función que demuestra polimorfismo
def mostrar_roles(personas):
    print("\n=== POLIMORFISMO - ROLES DE PERSONAS ===")
    for persona in personas:
        print(f"- {persona._nombre} {persona._apellido}: {persona.obtener_rol()}")

# CASOS DE PRUEBA
def main():
    print(" SISTEMA DE GESTIÓN UNIVERSITARIA")
    print("="*50)
   
    # 1. Crear universidad
    universidad = Universidad("Universidad Nacional de Tucumán", "Av. Independencia 1800", 1914)
   
    # 2. Crear departamentos (Composición)
    dept_informatica = Departamento("Informática", "INF", "Edificio A - Piso 3")
    dept_matematicas = Departamento("Matemáticas", "MAT", "Edificio B - Piso 2")
   
    universidad.agregar_departamento(dept_informatica)
    universidad.agregar_departamento(dept_matematicas)
   
    # 3. Crear profesores
    prof1 = Profesor("Carlos", "Perez", "20123456789", date(1980, 5, 15), "P001", "Informática", 10)
    prof2 = Profesor("Ana", "Martínez", "27987654321", date(1985, 8, 22), "P002", "Matemáticas", 8)
   
    # Agregación: Departamentos tienen profesores
    dept_informatica.agregar_profesor(prof1)
    dept_matematicas.agregar_profesor(prof2)
   
    # 4. Crear estudiantes
    est1 = Estudiante("Juan", "Pérez", "45123456789", date(2002, 3, 10), "E2024001", "Ingeniería en Sistemas", 2024)
    est2 = Estudiante("María", "López", "44987654321", date(2003, 7, 5), "E2024002", "Licenciatura en Matemáticas", 2024)
    est3 = Estudiante("Pedro", "Rodríguez", "43555666777", date(2001, 12, 20), "E2023015", "Ingeniería en Sistemas", 2023)
   
    # 5. Crear administrativo
    admin1 = Administrativo("Laura", "García", "25111222333", date(1978, 4, 12), "A001", "Académica", "Secretaria")
   
    # 6. Crear cursos
    curso1 = Curso("INF101", "Programación I", 6, "Lunes y Miércoles 14:00-16:00")
    curso2 = Curso("MAT201", "Cálculo II", 8, "Martes y Jueves 10:00-12:00")
    curso3 = Curso("INF301", "Base de Datos", 6, "Viernes 08:00-12:00")
   
    # 7. Asignar profesores a cursos (Asociación dirigida)
    prof1.dictar_curso(curso1)
    prof1.dictar_curso(curso3)
    prof2.dictar_curso(curso2)
   
    # 8. Inscribir estudiantes en cursos (Asociación simple)
    est1.inscribir_curso(curso1)
    est1.inscribir_curso(curso3)
    est2.inscribir_curso(curso2)
    est3.inscribir_curso(curso1)
    est3.inscribir_curso(curso3)
   
    # 9. Mostrar información del sistema
    universidad.mostrar_info()
   
    for dept in universidad._departamentos:
        dept.mostrar_info()
   
    for i, curso in enumerate([curso1, curso2, curso3], 1):
        curso.mostrar_info()
   
    # 10. Demostrar polimorfismo
    todas_las_personas = [prof1, prof2, est1, est2, est3, admin1]
    mostrar_roles(todas_las_personas)
   
    # 11. Información detallada de algunas personas
    print("\n=== INFORMACIÓN DETALLADA ===")
    print("\n--- PROFESOR ---")
    prof1.mostrar_info()
   
    print("\n--- ESTUDIANTE ---")
    est1.mostrar_info()
   
    print("\n--- ADMINISTRATIVO ---")
    admin1.mostrar_info()

if __name__ == "__main__":
    main()