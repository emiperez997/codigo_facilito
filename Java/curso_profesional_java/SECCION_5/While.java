package SECCION_5;

public class While {

  public static void main(String[] args) {
    // while → mientras
    // do while → hacer mientras
    // int contador = 1;
    // while (contador < 11) {
    // System.out.println("Hola mundo " + contador);
    // contador++;
    // }

    int contador = 0;

    // Primero se ejecuta el código y luego se evalúa la condición
    do {
      System.out.println("Hola mundo " + contador);
      contador++;
    } while (contador < 11);

  }
}
