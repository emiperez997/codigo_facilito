package SECCION_4;

public class CompararCadenas {

  public static void main(String[] args) {
    String cadena1 = "Hola";
    String cadena2 = "hola";

    // Comparar cadenas
    // Si son exactamente iguales devuelve true
    // Si no son exactamente iguales devuelve false
    boolean isEqual = cadena1.toUpperCase().equals(cadena2.toUpperCase()); // Devuelve un booleano

    System.out.println(isEqual);

    String nuevaCadena1 = cadena1.toUpperCase();
    String nuevaCadena2 = cadena2.toUpperCase();

    // equalsIgnoreCase → Compara cadenas sin importar si son mayúsculas o
    // minúsculas

    boolean resultado = cadena1.equalsIgnoreCase(nuevaCadena2);
    System.out.println(resultado);

  }
}
