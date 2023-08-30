package SECCION_4;

public class MetodosString {

  public static void main(String[] args) {

    // Métodos → Funciones que tiene la clase String
    String mensaje = "Hola, soy un String";

    int cantidad = mensaje.length(); // Devuelve la longitud del String en Int

    // Devuelve un booleano si el String contiene la palabra "Hola"
    boolean contiene = mensaje.contains("Hola");

    boolean comienzaCon = mensaje.startsWith("H");
    boolean terminaCon = mensaje.endsWith("g");

    String nuevoStrings = mensaje.concat(". Adios"); // No modifica el String original

    System.out.println(cantidad);
    System.out.println(contiene);
    System.out.println(comienzaCon);
    System.out.println(terminaCon);
    System.out.println(nuevoStrings);

  }
}
