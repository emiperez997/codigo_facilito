package SECCION_2;

public class Variables {

  public static void main(String[] args) {
    // Tipos de datos
    // - Integers
    // - Floating point
    // - Characters
    // - Booleans

    // Tipo de Dato NombreVariable = Valor;
    int version; // → Reservamos espacio en memoria para un entero
    version = 8; // → Asignamos el valor 8 a la variable version
    version = 9; // → Podemos reasignar el valor de la variable cuantas veces queramos
    System.out.println(version);

    // Se utiliza la convención de nombres camelCase para nombrar variables
    int versionJava = 9; // → Podemos declarar y asignar el valor de una variable en una sola linea
    System.out.println(versionJava);

    int[] arreglo = new int[10];

    int valor = arreglo[0];
    System.out.println(valor);

  }
}
