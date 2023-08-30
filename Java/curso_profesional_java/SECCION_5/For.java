package SECCION_5;

public class For {

  public static void main(String[] args) {
    // for → para
    // for (inicializacion; condicion; iteracion) {}
    // inicializacion → Se ejecuta una sola vez
    // condicion → Se evalua cada vez que se ejecuta el código
    // iteracion → Se puede agregar más de una iteración separando por comas

    // Ningún apartado es obligatorio

    // for (int i = 0; i < 10; i++) {
    // System.out.println("Hola mundo " + i);
    // }

    // for (int numero = 9, x = 1; x <= 11; System.out.println(numero * x), x++) {}

    // for (int numero = 9, x = 1; x <= 10; x++) {
    // int resultado = numero * x;
    // String mensaje = numero + " x " + x + " = " + resultado;
    // System.out.println(mensaje);
    // }

    for (int numero = 1; numero < 101; numero++) {
      if (numero % 2 == 0) {
        System.out.println(numero);
      }
    }
  }

}
