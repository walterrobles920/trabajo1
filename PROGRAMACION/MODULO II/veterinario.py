# Clase Corazón - Composición con Mascota
class Corazon {
    private int frecuenciaCardiaca;
    
    public Corazon(int frecuenciaCardiaca) {
        this.frecuenciaCardiaca = frecuenciaCardiaca;
    }
    
    public int getFrecuenciaCardiaca() {
        return frecuenciaCardiaca;
    }
    
    public void setFrecuenciaCardiaca(int frecuenciaCardiaca) {
        this.frecuenciaCardiaca = frecuenciaCardiaca;
    }
    
    public boolean latir() {
        return frecuenciaCardiaca > 0;
    }
}

// Clase abstracta Mascota - Herencia y Abstracción
abstract class Mascota {
    // Encapsulamiento - atributos privados
    private String nombre;
    private int edad;
    private Corazon corazon; // Composición: sin corazón no puede vivir
    
    public Mascota(String nombre, int edad, int frecuenciaCardiaca) {
        this.nombre = nombre;
        this.edad = edad;
        this.corazon = new Corazon(frecuenciaCardiaca); // Composición obligatoria
    }
    
    // Getters y setters - Encapsulamiento
    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public int getEdad() {
        return edad;
    }
    
    public void setEdad(int edad) {
        this.edad = edad;
    }
    
    public Corazon getCorazon() {
        return corazon;
    }
    
    // Método común para todas las mascotas
    public void comer() {
        System.out.println(nombre + " está comiendo");
    }
    
    // Método abstracto - debe ser implementado por las clases hijas
    public abstract double calcularCostoConsulta();
    
    // Método abstracto para polimorfismo
    public abstract void hacerSonido();
    
    // Método para mostrar información básica
    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad + " años");
        System.out.println("Frecuencia cardíaca: " + corazon.getFrecuenciaCardiaca() + " lpm");
        System.out.println("Estado: " + (corazon.latir() ? "Vivo" : "Sin signos vitales"));
    }
    
    public boolean estaVivo() {
        return corazon.latir();
    }
}

#Clase Perro - Herencia de Mascota
class Perro extends Mascota {
    private String raza;
    
    public Perro(String nombre, int edad, String raza, int frecuenciaCardiaca) {
        super(nombre, edad, frecuenciaCardiaca);
        this.raza = raza;
    }
    
    public String getRaza() {
        return raza;
    }
    
    public void setRaza(String raza) {
        this.raza = raza;
    }
    
    // Polimorfismo - implementación específica
    @Override
    public void hacerSonido() {
        System.out.println(getNombre() + " dice: ¡Guau guau!");
    }
    
    // Abstracción - implementación del método abstracto
    @Override
    public double calcularCostoConsulta() {
        // Los perros tienen costo base + extra por raza grande
        double costoBase = 25.0;
        if (raza.toLowerCase().contains("pastor") || 
            raza.toLowerCase().contains("labrador") || 
            raza.toLowerCase().contains("golden")) {
            costoBase += 10.0; // Razas grandes cuestan más
        }
        return costoBase;
    }
    
    @Override
    public void mostrarInfo() {
        System.out.println("=== INFORMACIÓN DEL PERRO ===");
        super.mostrarInfo();
        System.out.println("Raza: " + raza);
        System.out.println("Costo consulta: $" + calcularCostoConsulta());
    }
}

#Clase Gato - Herencia de Mascota
class Gato extends Mascota {
    private String colorPelo;
    
    public Gato(String nombre, int edad, String colorPelo, int frecuenciaCardiaca) {
        super(nombre, edad, frecuenciaCardiaca);
        this.colorPelo = colorPelo;
    }
    
    public String getColorPelo() {
        return colorPelo;
    }
    
    public void setColorPelo(String colorPelo) {
        this.colorPelo = colorPelo;
    }
    
    // Polimorfismo - implementación específica
    @Override
    public void hacerSonido() {
        System.out.println(getNombre() + " dice: ¡Miau miau!");
    }
    
    // Abstracción - implementación del método abstracto
    @Override
    public double calcularCostoConsulta() {
        // Los gatos tienen costo fijo
        return 20.0;
    }
    
    @Override
    public void mostrarInfo() {
        System.out.println("=== INFORMACIÓN DEL GATO ===");
        super.mostrarInfo();
        System.out.println("Color de pelo: " + colorPelo);
        System.out.println("Costo consulta: $" + calcularCostoConsulta());
    }
}

#Clase Dueño - Asociación uno a muchos con Mascota
class Dueño {
    private String nombre;
    private String telefono;
    private java.util.List<Mascota> mascotas;
    
    public Dueño(String nombre, String telefono) {
        this.nombre = nombre;
        this.telefono = telefono;
        this.mascotas = new java.util.ArrayList<>();
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public String getTelefono() {
        return telefono;
    }
    
    public void agregarMascota(Mascota mascota) {
        mascotas.add(mascota);
    }
    
    public void removerMascota(Mascota mascota) {
        mascotas.remove(mascota);
    }
    
    public java.util.List<Mascota> getMascotas() {
        return new java.util.ArrayList<>(mascotas); // Copia defensiva
    }
    
    public void mostrarMascotas() {
        System.out.println("Dueño: " + nombre + " (Tel: " + telefono + ")");
        System.out.println("Mascotas:");
        if (mascotas.isEmpty()) {
            System.out.println("  No tiene mascotas registradas");
        } else {
            for (Mascota mascota : mascotas) {
                System.out.println("  - " + mascota.getNombre() + 
                                 " (" + mascota.getClass().getSimpleName() + ")");
            }
        }
    }
}

# Clase Veterinaria - Agregación con Mascota
class Veterinaria {
    private String nombre;
    private java.util.List<Mascota> mascotasEnAtencion;
    private boolean abierta;
    
    public Veterinaria(String nombre) {
        this.nombre = nombre;
        this.mascotasEnAtencion = new java.util.ArrayList<>();
        this.abierta = true;
    }
    
    public void atenderMascota(Mascota mascota) {
        if (!abierta) {
            System.out.println("La veterinaria está cerrada");
            return;
        }
        
        if (!mascota.estaVivo()) {
            System.out.println("¡EMERGENCIA! " + mascota.getNombre() + 
                             " necesita atención inmediata - sin signos vitales");
            return;
        }
        
        mascotasEnAtencion.add(mascota);
        System.out.println("Atendiendo a " + mascota.getNombre() + 
                         " en " + nombre);
    }
    
    public void realizarConsulta(Mascota mascota) {
        if (!mascotasEnAtencion.contains(mascota)) {
            System.out.println("La mascota no está en atención");
            return;
        }
        
        System.out.println("\n--- CONSULTA VETERINARIA ---");
        mascota.mostrarInfo();
        mascota.hacerSonido(); // Polimorfismo en acción
        System.out.println("Total a pagar: $" + mascota.calcularCostoConsulta());
    }
    
    public void darDeAlta(Mascota mascota) {
        mascotasEnAtencion.remove(mascota);
        System.out.println(mascota.getNombre() + " ha sido dado de alta");
    }
    
    public void cerrarVeterinaria() {
        this.abierta = false;
        System.out.println("Veterinaria " + nombre + " cerrada.");
        System.out.println("Las mascotas siguen existiendo independientemente.");
        // Las mascotas no se eliminan - solo se pierde la referencia débil
        mascotasEnAtencion.clear();
    }
    
    public void abrirVeterinaria() {
        this.abierta = true;
        System.out.println("Veterinaria " + nombre + " abierta.");
    }
    
    public boolean estaAbierta() {
        return abierta;
    }
    
    public void mostrarMascotasEnAtencion() {
        System.out.println("Mascotas en atención en " + nombre + ":");
        if (mascotasEnAtencion.isEmpty()) {
            System.out.println("  No hay mascotas en atención");
        } else {
            for (Mascota mascota : mascotasEnAtencion) {
                System.out.println("  - " + mascota.getNombre() + 
                                 " (" + mascota.getClass().getSimpleName() + ")");
            }
        }
    }
}

#Clase principal para demostrar el funcionamiento
public class SistemaMascotas {
    public static void main(String[] args) {
        System.out.println("=== SISTEMA DE MASCOTAS - VETERINARIA ===\n");
        
        // Crear veterinaria
        Veterinaria vetSanRoque = new Veterinaria("Veterinaria San Roque");
        
        // Crear dueños
        Dueño maria = new Dueño("María González", "123-456-789");
        Dueño carlos = new Dueño("Carlos Rodríguez", "987-654-321");
        
        // Crear mascotas - Demostrar composición (cada mascota DEBE tener corazón)
        Perro firulais = new Perro("Firulais", 3, "Labrador", 80);
        Gato michi = new Gato("Michi", 2, "Naranja", 120);
        Perro rex = new Perro("Rex", 5, "Pastor Alemán", 75);
        Gato luna = new Gato("Luna", 1, "Negro", 130);
        
        // Establecer relaciones Dueño-Mascota (Asociación)
        maria.agregarMascota(firulais);
        maria.agregarMascota(michi);
        carlos.agregarMascota(rex);
        carlos.agregarMascota(luna);
        
        // Mostrar información de dueños y sus mascotas
        System.out.println("1. INFORMACIÓN DE DUEÑOS Y SUS MASCOTAS:");
        System.out.println("----------------------------------------");
        maria.mostrarMascotas();
        System.out.println();
        carlos.mostrarMascotas();
        System.out.println();
        
        // Demostrar polimorfismo con un array de mascotas
        System.out.println("2. DEMOSTRACIÓN DE POLIMORFISMO:");
        System.out.println("---------------------------------");
        Mascota[] mascotas = {firulais, michi, rex, luna};
        
        for (Mascota mascota : mascotas) {
            System.out.println("\n" + mascota.getNombre() + ":");
            mascota.hacerSonido(); // Polimorfismo: cada tipo hace sonido diferente
            mascota.comer();
            System.out.println("Costo consulta: $" + mascota.calcularCostoConsulta());
        }
        
        System.out.println("\n3. ATENCIÓN VETERINARIA:");
        System.out.println("------------------------");
        
        // Atender mascotas en la veterinaria (Agregación)
        vetSanRoque.atenderMascota(firulais);
        vetSanRoque.atenderMascota(michi);
        vetSanRoque.mostrarMascotasEnAtencion();
        
        System.out.println();
        
        // Realizar consultas
        vetSanRoque.realizarConsulta(firulais);
        System.out.println();
        vetSanRoque.realizarConsulta(michi);
        
        // Dar de alta
        System.out.println();
        vetSanRoque.darDeAlta(firulais);
        vetSanRoque.mostrarMascotasEnAtencion();
        
        System.out.println("\n4. DEMOSTRACIÓN DE AGREGACIÓN:");
        System.out.println("-------------------------------");
        System.out.println("Estado antes de cerrar:");
        System.out.println("Firulais está vivo: " + firulais.estaVivo());
        System.out.println("Michi está vivo: " + michi.estaVivo());
        
        // Cerrar veterinaria - las mascotas siguen existiendo (agregación débil)
        vetSanRoque.cerrarVeterinaria();
        
        System.out.println("\nEstado después de cerrar veterinaria:");
        System.out.println("Firulais está vivo: " + firulais.estaVivo());
        System.out.println("Michi está vivo: " + michi.estaVivo());
        System.out.println("Las mascotas siguen existiendo independientemente de la veterinaria.");
        
        System.out.println("\n5. DEMOSTRACIÓN DE COMPOSICIÓN:");
        System.out.println("--------------------------------");
        System.out.println("Información del corazón de Firulais:");
        System.out.println("Frecuencia cardíaca: " + firulais.getCorazon().getFrecuenciaCardiaca());
        
        // Simular problema cardíaco
        firulais.getCorazon().setFrecuenciaCardiaca(0);
        System.out.println("Después de problema cardíaco:");
        System.out.println("Firulais está vivo: " + firulais.estaVivo());
        
        // Intentar atender mascota sin signos vitales
        vetSanRoque.abrirVeterinaria();
        vetSanRoque.atenderMascota(firulais);
        
        System.out.println("\n6. INFORMACIÓN DETALLADA DE MASCOTAS:");
        System.out.println("--------------------------------------");
        rex.mostrarInfo();
        System.out.println();
        luna.mostrarInfo();
    }
}