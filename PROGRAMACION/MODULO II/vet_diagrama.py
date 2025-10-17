from graphviz import Digraph

# Crear el diagrama
dot = Digraph(comment='Diagrama de Clases - Sistema de Mascotas')
dot.attr(rankdir='BT')  # Dirección de arriba hacia abajo

# Clase abstracta Mascota
dot.node('Mascota', '''<<abstract>> Mascota
- __nombre: str
- __edad: int
- __corazon: Corazon
- __dueño: Dueno
+ get_nombre(): str
+ get_edad(): int
+ get_corazon(): Corazon
+ get_dueño(): Dueno
+ calcular_costo_consulta(): float
+ hacer_sonido(): void
+ mostrar_info(): void
+ comer(): void''', shape='record')

# Clase Perro
dot.node('Perro', '''Perro
- __raza: str
+ hacer_sonido(): void
+ calcular_costo_consulta(): float
+ mostrar_info(): void''', shape='record')

# Clase Gato
dot.node('Gato', '''Gato
- __color_pelo: str
+ hacer_sonido(): void
+ calcular_costo_consulta(): float
+ mostrar_info(): void''', shape='record')

# Clase Corazon
dot.node('Corazon', '''Corazon
- __frecuencia_cardiaca: int
+ get_frecuencia_cardiaca(): int
+ set_frecuencia_cardiaca(frecuencia): void''', shape='record')

# Clase Dueno
dot.node('Dueno', '''Dueno
- __nombre: str
- __telefono: str
- __mascotas: list
+ get_nombre(): str
+ get_telefono(): str
+ agregar_mascota(mascota): void
+ listar_mascotas(): void''', shape='record')

# Clase Veterinaria
dot.node('Veterinaria', '''Veterinaria
- __nombre: str
- __mascotas: list
+ agregar_mascota(mascota): void
+ listar_mascotas(): void''', shape='record')

# Relaciones
dot.edge('Perro', 'Mascota', arrowhead='empty')        # Herencia
dot.edge('Gato', 'Mascota', arrowhead='empty')         # Herencia
dot.edge('Mascota', 'Corazon', label='1', arrowhead='diamond')     # Composición
dot.edge('Mascota', 'Dueno', label='1', arrowhead='normal')        # Asociación
dot.edge('Dueno', 'Mascota', label='*', arrowhead='normal')
dot.edge('Veterinaria', 'Mascota', label='*', arrowhead='odiamond')  # Agregación

# Guardar o visualizar
dot.render('diagrama_mascotas', format='png', cleanup=True)  # Guarda como PNG
