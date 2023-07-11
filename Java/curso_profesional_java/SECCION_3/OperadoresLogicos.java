package SECCION_3;

public class OperadoresLogicos {

  public static void main(String[] args) {
    // Operadores lógicos
    // and (y), or (o) y not (no)

    boolean resultado;

    resultado = 5 >= 5 && true && 10 > 5;
    System.out.println(resultado);

    resultado = false || false || false || true;
    System.out.println(resultado);

    resultado = (5 >= (2 * 3) || true) && (10 > 5 && true);
    System.out.println(resultado);

    System.out.println(!true); // → false. Negación
  }
}
