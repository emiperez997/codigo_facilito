package SECCION_4;

public class MetodosFormato {

  public static void main(String[] args) {
    // Parte 1
    // String mensaje = " Hola, soy un String";

    // System.out.println(mensaje.toUpperCase()); // Convierte el String a
    // mayúsculas
    // System.out.println(mensaje.toLowerCase()); // Convierte el String a
    // minúsculas

    // System.out.println(mensaje.trim()); // Elimina los espacios en blanco al
    // inicio y al final del String

    // System.out.println(mensaje.toUpperCase().trim()); // Se pueden encadenar
    // métodos

    // System.out.println(mensaje);

    // Parte 2

    String mensaje = "";
    String curso = "Java";

    float valor = 10.3456f;

    // Genera un nuevo String con el valor de la variable mensaje
    // mensaje = String.format("Bienvenido al curso %s", curso);
    // mensaje = String.format("%.2f", valor); // Redondea el valor a 2 decimales
    // %.2f → 2 decimales

    // %d → Entero
    // %s → String
    // %f → Float

    mensaje = String.format("El total de %d articulos es %.4f %s", 3, valor, curso);
    System.out.println(mensaje);

    // No genera un nuevo String con el valor de la variable mensaje
    System.out.printf("El total de %d articulos es %.4f %s", 3, valor, curso);
  }
}
