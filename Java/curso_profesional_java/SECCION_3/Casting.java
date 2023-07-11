package SECCION_3;

public class Casting {

  public static void main(String[] args) {
    int variableX = 50;
    float variableZ = 5.5f;
    int resultado;

    // (int) → Casting a entero
    resultado = variableX + (int) variableZ;
    System.out.println("Suma: " + resultado);
    System.out.println((int) variableZ);

    resultado = (int) ((float) variableX + variableZ);
    System.out.println("Suma: " + resultado);
    System.out.println((int) variableZ);
  }
}
